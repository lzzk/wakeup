# Wekeup Bot 


todo

## Basic Usage

```yaml
name: wekeuppppp

on:
  workflow_dispatch:

jobs:
  wakeup:
    name: wekeup bot
    runs-on: ubuntu-latest
    steps:
      - name: Wekeup
        uses: godruoyi/wekeup@main
        with:
          bing_auth_token: ${{ secrets.BING_AUTH_TOKEN }}
          tg_token: ${{ secrets.TG_TOKEN }}
          tg_chat_id: ${{ secrets.TG_CHAT_ID }}
          weather_city: ${{ secrets.CITY }}
```

## Thanks

- @yihong0618
- @BennyThink
- @xenv


## Appreciation

- Thank you, that's enough. Just enjoy it.
