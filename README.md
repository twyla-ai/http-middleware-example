# Twyla HTTP Integration Middleware Template: Zeit Now

This is a template repository to build Twyla HTTP integration middleware services for 
deployment on [ZEIT Now](https://zeit.co/). These services allow for flexible 
integrations with third-party services and data sources within your conversations 
designed using [Twyla Canvas](https://canvas.twyla.ai/). 

This could also be used as an example for deployment of [Starlette](https://www.starlette.io/) 
[ASGI](https://channels.readthedocs.io/en/latest/asgi.html) application on Zeit.

## Quick Start
Note that we assume you already have a [ZEIT Account](https://zeit.co/login) that is 
[linked to your GitHub account](https://zeit.co/docs/v2/advanced/now-for-github/).

1. [Create a GitHub repository using this template](https://github.com/twyla-ai/http-middleware-zeit-template/generate).
2. [Import your new repository as a new project in ZEIT](https://zeit.co/new?#import-github).

That should be it. ZEIT should have a deployment built and ready for you in no time.

## Notes
* The `now.json` file is not strictly required as this will work with zero-config as well. We use this to enable some route redirection.
* Since ZEIT passes the path as is to the application, the application should handle path prefixes like `/api`.
* Endpoints deployed here are not secured. This means, they rely on obscurity or the 
deployment URL to remain private. If endpoints do need to be secured, look into how to 
integrate with  a stateless authentication mechanism/service (eg: [auth0](https://auth0.com/)).
Alternatively, allow for `Authorization` headers or tokens to be passed through to the 
backing service or data source. 

## References
* [ZEIT Configuration Documentation](https://zeit.co/docs/configuration/)
* [ZEIT Now Python Advanced Builder Documentation](https://zeit.co/docs/builders/#official-builders/python/python-dependencies)
* [Starlette Documentation](https://www.starlette.io/)
* [ZEIT Now Deployment Concepts](https://zeit.co/docs/v2/advanced/concepts/overview/)
