export default {
  async fetch(request, env) {
    const url = new URL(request.url);

    if (url.pathname === "/auth") {
      const authUrl = new URL("https://github.com/login/oauth/authorize");
      authUrl.searchParams.set("client_id", env.OAUTH_CLIENT_ID);
      authUrl.searchParams.set("scope", "repo,user");
      authUrl.searchParams.set("state", crypto.randomUUID());
      return Response.redirect(authUrl.toString(), 302);
    }

    if (url.pathname === "/callback") {
      const code = url.searchParams.get("code");
      if (!code) return new Response("Missing code", { status: 400 });

      const tokenRes = await fetch("https://github.com/login/oauth/access_token", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
          "Accept": "application/json",
        },
        body: JSON.stringify({
          client_id: env.OAUTH_CLIENT_ID,
          client_secret: env.OAUTH_CLIENT_SECRET,
          code,
        }),
      });

      const data = await tokenRes.json();
      if (data.error) {
        return new Response(JSON.stringify(data), { status: 400 });
      }

      const content = JSON.stringify({
        token: data.access_token,
        provider: "github",
      });

      const html = `<!doctype html><html><body><script>
        (function() {
          function receiveMessage(e) {
            window.opener.postMessage(
              'authorization:github:success:${content.replace(/'/g, "\\'")}',
              e.origin
            );
          }
          window.addEventListener("message", receiveMessage, false);
          window.opener.postMessage("authorizing:github", "*");
        })();
      </script></body></html>`;

      return new Response(html, {
        headers: { "Content-Type": "text/html;charset=UTF-8" },
      });
    }

    return new Response("Decap OAuth Proxy Running", { status: 200 });
  },
};