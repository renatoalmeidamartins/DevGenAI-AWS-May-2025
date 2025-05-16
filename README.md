# Repo with links for the Developing Generative AI applications on AWS

## Code sample
- Go [here](/code-sample)
- When running locally, ensure you create a virtual environment (```python -m env path-to-env```), and activate it (on Windows ```path-to-env/scripts/activate.ps1```)
- Run a ```pip install -r requirements.txt```
## Class evaluation
- Go to [aws.training](https://www.aws.training/)
- Click sign in, log in with the same account you used to access the lab and course materials
- Then go on the top right to My Account, then transcript, click on the Archived section (direct link [https://www.aws.training/Account/Transcript/Archived](https://www.aws.training/Account/Transcript/Archived)
- You should see the class, with a button to evaluate

## Links to access the class and materials
- [Meeting link](https://awsvirtual.webex.com/awsvirtual/j.php?MTID=m2e71924ae32964ae1fc324f3dbaba1c0)
- [Access to lab and books](https://us-east-1.student.classrooms.aws.training/class/ilt%235frpxG76eKHKUyzVzH4UTs)

## Supporting materials
- [AWS Skill builder](https://skillbuilder.aws/)
- [AWS technical essentials](https://explore.skillbuilder.aws/learn/courses/1851/aws-technical-essentials)
- [All courses available from AWS training and certification](https://releases.awstc.com/)

## Day 1 links
- [Artificial neuron](https://en.wikipedia.org/wiki/Artificial_neuron)
- [Perceptron](https://en.wikipedia.org/wiki/Perceptron)
- [Neural network zoo](https://www.asimovinstitute.org/neural-network-zoo/)
- [Sagemaker built-in models](https://docs.aws.amazon.com/sagemaker/latest/dg/algos.html)
- [AWS Comprehend Sentiment analysis](https://docs.aws.amazon.com/comprehend/latest/dg/how-sentiment.html)
- [Responsible Ai](https://aws.amazon.com/ai/responsible-ai/policy/)
- [Lllama model leak into 4chan](https://www.theverge.com/2023/3/8/23629362/meta-ai-language-model-llama-leak-online-misuse)
- [Transformers in neural networks](https://aws.amazon.com/what-is/transformers-in-artificial-intelligence/)
- Some examples of models harming people:
  - https://www.tradingview.com/news/cointelegraph:0909bdece094b:0-researchers-hack-ai-enabled-robots-to-cause-real-world-harm/
  - https://www.tomshardware.com/tech-industry/artificial-intelligence/researchers-jailbreak-ai-robots-to-run-over-pedestrians-place-bombs-for-maximum-damage-and-covertly-spy
  - https://unit42.paloaltonetworks.com/new-frontier-of-genai-threats-a-comprehensive-guide-to-prompt-attacks/
  - https://www.wired.com/story/researchers-llm-ai-robot-violence/
- [Jailbreaking model research](https://unit42.paloaltonetworks.com/jailbreaking-generative-ai-web-products/)
- [AWS Shared responsibility model](https://aws.amazon.com/compliance/shared-responsibility-model/)
- [Quotas for Bedrock](https://docs.aws.amazon.com/general/latest/gr/bedrock.html#limits_bedrock)
- [Model availability by region for Bedrock](https://docs.aws.amazon.com/bedrock/latest/userguide/models-regions.html)
- [Macie is a good service for identifying PII](https://docs.aws.amazon.com/macie/latest/user/data-classification.html)
- [Bedrock on-demand pricing](https://aws.amazon.com/bedrock/pricing/)

## Day 2 links
- [Inferentia, custom-built inferencing chip](https://aws.amazon.com/ai/machine-learning/inferentia/)
- [Traininum, custom-buil AI training chip](https://aws.amazon.com/ai/machine-learning/trainium/)
- [GPU-powered instances](https://aws.amazon.com/ec2/instance-types/g5/)
- [GPT - Generative Pre-trained Transformers](https://aws.amazon.com/what-is/gpt/)
- [Stable diffusion announcement, image generation model](https://www.lmu.de/en/newsroom/news-overview/news/revolutionizing-image-generation-by-ai-turning-text-into-images.html)
- [Bedrock-runtime CLI](https://docs.aws.amazon.com/cli/latest/reference/bedrock-runtime/)
- Sample code for invoking a model through the CLI:
  ```
  aws bedrock-runtime invoke-model --model-id 'amazon.titan-text-premier-v1:0' --body '{  "inputText": "how to boil an egg?", "textGenerationConfig": { "maxTokenCount": 2048, "temperature": 1 } }' --cli-binary-format raw-in-base64-out C:\tmp\outfile.txt
  ```
- [Inference parameters for all model "families"](https://docs.aws.amazon.com/bedrock/latest/userguide/model-parameters.html)
- Minimimum permission required to invoke a model (in the example below, we can invoke all models, as resource is *:
```
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Sid": "VisualEditor0",
            "Effect": "Allow",
            "Action": "bedrock:InvokeModel",
            "Resource": "*"
        }
    ]
}
```
- [Prompt engineering guide](https://www.promptingguide.ai/)
- [Leaked system prompts, along with links to the techniques used to make them leak](https://github.com/jujumilk3/leaked-system-prompts)
- Vector databases
  - [Azure list of open source vector databases](https://learn.microsoft.com/en-us/azure/cosmos-db/mongodb/vcore/vector-search-ai)
  - [AWS info on vector databases, and how their own services can be used to store vector data](https://aws.amazon.com/what-is/vector-databases/)
  - [FAISS, an open source vector DB from Facebook](https://github.com/facebookresearch/faiss)


## Day 3 links
- [LangChain documentation](https://python.langchain.com/docs/introduction/)
- [Better browsing through the tutorials](https://python.langchain.com/docs/tutorials/)
- [Inside GitHub there are plenty of sample notebooks - go into cookbooks and docs folder](https://github.com/langchain-ai/langchain)
- [Rate limiters could be used with LangChain](https://python.langchain.com/docs/how_to/chat_model_rate_limiting/)
