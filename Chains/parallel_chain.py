from langchain_aws import ChatBedrockConverse
from langchain_ollama import ChatOllama
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_classic.schema.runnable import RunnableParallel

load_dotenv()

model1= ChatBedrockConverse(
    model_id="nvidia.nemotron-nano-3-30b",
    region_name="us-east-1"
)

model2=ChatOllama(model="llama3:8b")

prompt1=PromptTemplate(
    template="Generate a short and simple notes form the following text \n {text} ",
    input_variables=['text'],
    
)
prompt2=PromptTemplate(
    template="Generate 5 short question answers  from the following  text \n {text} ",
    input_variables=['text'],)

prompt3=PromptTemplate(
    template="Merge the provided notes and quiz into a single document ]n notes -> {notes} and quiz ->{quiz} ",
    input_variables=['notes','quiz'])   

parser=StrOutputParser()

parallel_chain=RunnableParallel({
    'notes': prompt1 | model1 | parser,
    'quiz': prompt2 | model2 | parser
})

merge_chain= prompt3 | model2 | parser

chain= parallel_chain | merge_chain

text="""
DynamoDB addresses your needs to overcome scaling and operational complexities of relational databases. 
DynamoDB is purpose-built and optimized for operational workloads that require consistent performance at any scale. For example, DynamoDB delivers consistent single-digit millisecond performance for a shopping cart use case,
whether you have 10 or 100 million users. 
Launched in 2012, DynamoDB continues to help you move away from relational databases while reducing cost and improving performance at scale.

Customers across all sizes, industries, and geographies use DynamoDB to build modern, serverless applications that can start small and scale globally. DynamoDB scales to 
support tables of virtually any size while providing consistent single-digit millisecond performance and high availability.

For events, such as Amazon Prime Day, DynamoDB powers multiple high-traffic Amazon properties and systems, including Alexa, Amazon.com sites, and all Amazon fulfillment centers. 
For such events, DynamoDB APIs have handled trillions of calls from Amazon properties and systems. DynamoDB continuously serves hundreds of customers with tables that have peak traffic of over half a million requests per second. 
It also serves hundreds of customers whose table sizes exceed 200 TB, and processes over one billion requests per hour.

Topics
Characteristics of DynamoDB

DynamoDB use cases

Capabilities of DynamoDB

Service integrations

Security

Resilience

Accessing DynamoDB

DynamoDB pricing

Getting started with DynamoDB

Characteristics of DynamoDB

Serverless
With DynamoDB, you don't need to provision any servers, or patch, manage, install, maintain, or operate any software. DynamoDB provides zero downtime maintenance. 
It has no versions (major, minor, or patch), and there are no maintenance windows.

DynamoDB's on-demand capacity mode offers pay-as-you-go pricing for read and write requests so you only pay for what you use. With on-demand, DynamoDB instantly scales
up or down your tables to adjust for capacity and maintains performance with zero administration. It also scales down to zero so you don't pay for throughput when your 
table doesn't have traffic and there are no cold starts.

NoSQL
As a NoSQL database, DynamoDB is purpose-built to deliver improved performance, scalability, manageability, and flexibility compared to traditional relational databases. 
To support a wide variety of use cases, DynamoDB supports both key-value and document data models.

Unlike relational databases, DynamoDB doesn't support a JOIN operator. We recommend that you denormalize your data model to reduce database round trips and processing power needed to answer queries. 
As a NoSQL database, DynamoDB provides strong read consistency and ACID transactions to build enterprise-grade applications.

Fully managed
As a fully managed database service, DynamoDB handles the undifferentiated heavy lifting of managing a database so that you can focus on building value for your customers. 
It handles setup, configurations, maintenance, high availability, hardware provisioning, security, backups, monitoring, and more. This ensures that when you create a DynamoDB table, it's instantly ready for production workloads. 
DynamoDB constantly improves its availability, reliability, performance, security, and functionality without requiring upgrades or downtime.

Single-digit millisecond performance at any scale
DynamoDB was purpose-built to improve upon the performance and scalability of relational databases to deliver single-digit millisecond performance at any scale. 
To achieve this scale and performance, DynamoDB is optimized for high-performance workloads and provides APIs that encourage efficient database usage. 
It omits features that are inefficient and non-performing at scale, for example, JOIN operations. DynamoDB delivers consistent single-digit millisecond performance for your application, whether you have 100 or 100 million users.
"""

result=chain.invoke({'text':text})

print(result)



