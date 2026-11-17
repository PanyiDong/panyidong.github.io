## This is my personal website, please visit [https://panyidong.github.io/](https://panyidong.github.io/).

### Run locally

Requires Ruby and Bundler. Gems are installed into `vendor/bundle` (git-ignored).

```bash
bundle config set --local path vendor/bundle   # one-time
bundle install                                 # one-time, and after Gemfile changes
bundle exec jekyll serve -l                    # http://localhost:4000, live reload
```

Always use `bundle exec jekyll`, not a globally installed `jekyll`. Restart the server after editing `_config.yml`.

Alternatively, with Docker: `docker compose up --build`.

### Link checking

`.github/workflows/check-links.yml` builds the site and checks all links on every push, on pull requests, and weekly. Hosts that block automated checkers are excluded in `lychee.toml`.
