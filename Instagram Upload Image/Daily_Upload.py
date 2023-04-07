
import openai

# https://platform.openai.com/account/api-keys
API_Key = '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'
openai.api_key = API_Key

# list models
models = openai.Model.list()

image_resp = openai.Image.create(prompt="Minecraft Creeper, oil painting", 
                n=4, size="512x512")
print(image_resp)
