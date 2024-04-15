
## Project Background

OptimAI Customer Service Bot is a project developed on the pea.ai platform, aiming to provide efficient support services for users of the Optimism blockchain. The bot utilizes information from Optimism's official docs and Discord chat records, and uses ChatGPT for filtering and cleaning to extract high-quality Q&A content.

## Features

- Intelligent replies using information from Optimism's official docs and Discord chat records
- ChatGPT for information cleaning to provide high-quality user support services
- Rapid, accurate problem-solving and technical support for users

## Prepare Data

### 1. Download Chat Records from Discord

Use [DiscordChatExporter](https://github.com/Tyrrrz/DiscordChatExporter) 

```bash
docker run --rm -it -v ~/discord:/out tyrrrz/discordchatexporter:stable export -t DISCORD_TOKEN -c 667044844366987296 
```
docs
https://github.com/Tyrrrz/DiscordChatExporter/blob/master/.docs/Token-and-IDs.md

### 2. Clean Chat Records
The downloaded chat records are in HTML format, and we need to convert them to a text (txt) format.


```bash
python3 clean_discord_chat.py
```

The result will be saved in `data/discord_chat.txt`.

## Create Pea GPT
Please follow the instructions in the [PeaAI documentation](https://docs.pea.ai/docs/create-custom-gpt) to create a Pea GPT service.

Upload discord_chat.txt to the DataSet, and Pea GPT will automatically train on it. Once the training is complete, you can start using it.

You can also add websites like https://docs.optimism.io/ to the DataSet to provide Pea GPT with more information.

## Usage
Go to https://app.pea.ai/explore/all?search=OptimAI, search for "OptimAI," and then Subscribe to start chatting.

You can click on recommended questions or ask anything you like.



## License

This project is licensed under the [MIT License](LICENSE).
