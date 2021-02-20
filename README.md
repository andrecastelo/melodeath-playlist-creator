Hey there. This is a simple project by a metalhead for metalheads. The idea
behind it is simple: scrape Metal Archives for any melodic death metal
releases this month and create a playlist in Spotify from the results.

If you want to try this, you'll need a `client_id` and `client_secret` from
Spotify, and you need to add them to a `.env` file, like so:

```
SPOTIFY_CLIENT_ID=blablabla
SPOTIFY_CLIENT_SECRET=blablabla
```

The script will redirect you to an OAuth flow, then will ask you to paste the
url you were redirected to in the terminal. After that, everything should
work fine.

It's important to note that this is a personal project and not intended for
any type of commercial use or even other people using, so you might run
into some issues.
