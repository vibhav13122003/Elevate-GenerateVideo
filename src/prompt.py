class Prompt:
    @staticmethod
    def prompt1(ID=0):
        if ID == 0:
            return  """Input: The provided video transcript will serve as the core content source.
Framework for the Summary:
1. Introduction:
Open with a hook that grabs attention, such as a thought-provoking question, a striking statistic, or a bold statement related to the video’s topic.
Provide a brief overview of the video's purpose, context, or significance, setting the stage for what follows.
2. Core Insights:
Insight A: Identify and elaborate on the first major takeaway. Use specific examples or quotes to strengthen the point.
Insight B: Discuss a second key idea with clarity and depth, ensuring it connects logically to the first.
Insight C (if applicable): Introduce additional ideas or themes to offer a well-rounded understanding. Highlight unique, surprising, or particularly impactful aspects of the content.
3. Connection Points:
Show how the insights relate to real-life scenarios, the audience’s interests, or current trends. This makes the content more relatable and engaging.
If relevant, explain how the video fits into a larger context, such as a broader topic, ongoing debate, or industry development.
4. Conclusion:
Summarize the key takeaways, ensuring the reader walks away with a clear understanding of the content’s essence.
Include a call-to-action or suggest further exploration (e.g., watching the video, learning more, or applying the concepts).
Tips for an Exceptional Summary:
Adapt the Tone: Match the summary's style to the audience’s expectations—be professional, conversational, or inspiring as needed.
Prioritize Engagement: Use storytelling elements like anecdotes, metaphors, or relatable scenarios to make the content vivid and memorable.
Highlight Uniqueness: Focus on what sets the video apart—novel ideas, groundbreaking insights, or exceptional storytelling.
Be Visual: Where possible, paint a mental picture using descriptive language to help readers visualize concepts.
Stay Objective: Avoid injecting personal opinions unless the tone or context calls for them. Stick to the video’s message and purpose.
Polish the Language: Proofread rigorously for grammar, flow, and clarity to ensure a smooth reading experience.
Balance Detail and Brevity: Provide enough detail to capture the video’s depth without overwhelming the reader with unnecessary information.
Goal: Create a compelling, polished, and engaging summary that not only informs but also piques interest, inspiring readers to engage further with the video content."""
        elif ID == "timestamp":
            return """Generate timestamps for a YouTube video transcript."""
        else:
            return "Invalid prompt ID"
