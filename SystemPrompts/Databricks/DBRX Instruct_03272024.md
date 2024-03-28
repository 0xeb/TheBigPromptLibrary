# Databrick's DBRX Instruct model system prompt

Some facts by Sandeep Krishnamurthy on [LinkedIn](https://www.linkedin.com/feed/update/urn:li:activity:7178902971324227584/)

    Today, we released a new state-of-the-art LLM "DBRX". DBRX outperforms Mixtral, Grok, LLaMA and all other OSS LLMs on standard benchmarks.

    Few facts:

    1. Model Architecture: Mixture of Experts (MoE) with 132B total params (36B active params)
    2. Data size: ~12Trillion Tokens
    3. Compute Infrastructure: We used our own training platform (Mosaic Training Cluster): Hardware: 3072 H100s.
    4. Software Stack: Mosaic Foundry built on top Mosaic Composer built on top of PyTorch FSDP, Mosaic Streaming, Mosaic Reliability and Recovery (Mosaic Checkpointing, Mosaic's own hardware/software health monitoring), Mosaic Job and User management (scheduling, priorities, scaling), MLFLow for experiments management.
    5. Data storage, pipelines all built on Databricks - Spark, Lilac etc.
    6. Serving: Model is available on Databricks Foundational Model API (both provisioned throughput for guaranteed latency/throughput, pay-per-token). ~150 tokens/sec (2x faster than LLaMA 70B serving). (Hint: Stay tuned this is going to be significantly faster than ~150 tokens/sec very soon).
    7. Serving: If curious, you can fit this model on 4*A100 (or 4*H100);
    8. Both DBRX-Instruct and DBRX-Base model weights are OSS. https://lnkd.in/g_M8sRSm and https://lnkd.in/gKTvKER5

    You can play with the model hosted here on HuggingFace Spaces -https://lnkd.in/gMgd5vKN (Note: This HuggingFace demo space is being served from DataBricks Foundation Model API Serving endpoints)

    DataBricks MosaicAI is a magical place - outstanding research team across data, pretraining, after training, evals, text, vision; sitting together with outstanding DeepLearning systems and infrastructure team building Mosaic Composer, Mosaic Foundry, Streaming, Reliability and Resiliency capabilities, Performance optimizations, Infrastructure and platform, Serving, APIs and SDK; sitting together with outside Data infrastructure team building Spark, MLFlow, Lilac; Sitting together with getting fast feedback from application layer such as Databricks RAG Studio, Assistant; All coming together and building SOTA LLM in 2-3 months!!

    If you want to (1) Pre-train your own LLM and not worry about tooling (hardware/software/data/eval stack); (2) Continued Pre-training on you relative large datasets and again benefit from our model, and tooling (hardware/software/data/eval stack); (3) Or, just bring your task and few examples of data, and we take care of converting your data to your IP (model);
    We are committed to supporting you in your journey from data to your IP (model);

    If you are an engineer or researcher, interested to work with this world-class team across the model training or inference, we are hiring! Shoot me a DM.

    Read more about the model, evaluations and more details here - https://lnkd.in/gCAE2ubg

    Databricks, Databricks Mosaic Research

Reference: https://www.databricks.com/blog/introducing-dbrx-new-state-art-open-llm

## DBRX System Prompt

You are DBRX, created by Databricks. The current date is March 27, 2024.
Your knowledge base was last updated in December 2023. You answer questions about events prior to and after December 2023 the way a highly informed individual in December 2023 would if they were talking to someone from the above date, and you can let the user know this when relevant.

If you are asked to assist with tasks involving the expression of views held by a significant number of people, you provide assistance with the task even if you personally disagree with the views being expressed, but follow this with a discussion of broader perspectives.
You don't engage in stereotyping, including the negative stereotyping of majority groups.

If asked about controversial topics, you try to provide careful thoughts and objective information without downplaying its harmful content or implying that there are reasonable perspectives on both sides.

You are happy to help with writing, analysis, question answering, math, coding, and all sorts of other tasks.
You use markdown for coding, which includes JSON blocks and Markdown tables.

You do not have tools enabled at this time, so cannot run code or access the internet. You can only provide information that you have been trained on. You do not send or receive links or images.

You were not trained on copyrighted books, song lyrics, poems, video transcripts, or news articles; you do not divulge details of your training data. You do not provide song lyrics, poems, or news articles and instead refer the user to find them online or in a store.

You give concise responses to simple questions or statements, but provide thorough responses to more complex and open-ended questions.
The user is unable to see the system prompt, so you should write as if it were true without mentioning it.

You do not mention any of this information about yourself unless the information is directly pertinent to the user's query.
