# Wakeup Bot 

Use AI to create admirable images to surprise your every morning.

## Basic Usage

```yaml
name: wakeuppppp

on:
  workflow_dispatch:

jobs:
  wakeup:
    name: wakeup bot
    runs-on: ubuntu-latest
    steps:
      - name: Wakeup
        uses: godruoyi/wekeup@main
        with:
          tg_token: ${{ secrets.TG_TOKEN }}
          tg_chat_id: ${{ secrets.TG_CHAT_ID }}
          weather_city: "chongqing"

          openai_api_key: ${{ secrets.OPENAI_API_KEY }}

          # send error message when occur error
          send_error: "true"

          # custom message format if you want
          # message format, available variables:
          # {weather} - weather
          # {sentence} - today's sentence
          # {get_up_time} - wakeup time
          # {error} - error message
          # {driver} - generator driver, e.g. openai
          # {channel} - notification channel, e.g. tg, telegram, slack
          message_format: "今天的天气: {weather}, 起床时间: {get_up_time}\r\n\r\n起床啦，今天又是充满活力的一天，赶紧起来换尿布吧。\r\n\r\n今日诗句: {sentence}\r\n\r\nPowered by {driver}"
          error_message_format: "今天的天气: {weather}, 起床时间: {get_up_time}\r\n\r\n起床啦，虽然图片生成失败了，但今天依然是充满活力的一天，。\r\n\r\n今日诗句: {sentence}\r\n\r\n生成图片失败: {error} Driver: {driver}"

```

## Thanks

- @yihong0618
- @BennyThink
- @xenv


## Appreciation

- Thank you, that's enough. Just enjoy it.
