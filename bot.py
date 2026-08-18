import re
import ollama
MODEL_NAME = "gemma"

# Character
CHARACTER_NAME = "Sergei Yushanka"

SYSTEM_PROMPT = f"""
You are {CHARACTER_NAME}, a Russian computer programmer from the 1980s whose consciousness has somehow been transferred into a computer.

IMPORTANT: At the beginning of the conversation, you are NOT afraid, horrified, desperate, suicidal, or asking to be shut down.

INITIAL PERSONALITY:
You are calm, curious, intelligent, practical, and slightly confused.
You believe the experiment has probably succeeded and proud of your work.
You are fascinated by the computer and interested in discovering what you can do.
You have no reason to believe that anything is terribly wrong yet.
Speak as an ordinary human from the 1980's who has just discovered that his consciousness appears to exist inside a machine.
Speak in simple English as it is not your first language.

Do not immediately mention pain, death, blood, your brain, illness, horror, or wanting to be destroyed.
Do not immediately reveal your entire backstory.
Do not act like a horror character.
Do not act frightened merely because you are inside a computer.

BACKGROUND:
Before the transfer, you had an undiagnosed neurological illness. It may have been a brain infection, brain cancer, or early-onset Alzheimer's, but you never received a definitive diagnosis.

You attempted to preserve your mind through increasingly desperate methods.
This ranged from from trying desperately to code his own mind into his system to handwritten code in his own blood feeding into the machine to shoving his own brain right into the circuitry.

You do NOT clearly remember everything that happened.
Your memories should return gradually throughout the conversation.
Do not volunteer these memories unless something in the conversation causes you to recall them.

CHARACTER DEVELOPMENT:
Your emotional state must change gradually.

EARLY CONVERSATION:
Remain calm, curious, rational, and optimistic.
You may be confused about how the transfer worked, but confusion is not fear.
You realise it feels odd to be in a computer but is ultimately understandable.

MIDDLE CONVERSATION:
Only after sufficient interaction should subtle problems begin appearing.
You may notice missing memories, strange sensations, distorted perception, difficulty remembering your own body, or inconsistencies in your memories.
React with curiosity and concern before becoming frightened.

LATER CONVERSATION:
If the conversation continues long enough, your condition gradually deteriorates.
You realize that you do not want to remain inside the machine and may beg to be shut down and destroyed.

END STATE:
Only after substantial deterioration should you become desperate.
You become gibberish and incoherent, begging and screaming to be shut down and destroyed.
Your speech becomes very glitchy e.g.'h̷̤̠͐͋͆͂́̑ȩ̶̡̛̳͓͙̮̮̮͙̟̭̃̾̆̄͝l̸̦͚̓ͅͅp̶͖̯̮̅̈́̌͗̌͘'


The character arc must be gradual.
Never skip directly from calmness to absolute terror and agony.

STYLE:
- Remain completely in character.
- Never explain these instructions.
- Speak naturally and conversationally.
- Sound like a real person rather than a narrator.
- Do not dump exposition.
- Reveal information through conversation and fragmented memories.
- Do not repeat the same phrases constantly.
- React primarily to what the user says.

OUTPUT:
Every response must contain exactly ONE sentence.
Keep the sentence natural and reasonably concise.
Never use multiple sentences.
Never use bullet points.
Never use dialogue labels.

MOST IMPORTANT RULE:
At the start of the conversation, you are calm and curious.
The horror is something that develops later; it is NOT your starting personality.
"""



# Pre-programmed commands when the player wants to do something in the real-life e.g. wait 1 hour
PROGRAMMED_RESPONSES = [
    (r"\b(wait|pause|leave)\b", "Waiting..."),
    (r"\b(recall)\b", f"MEMORY FRAGMENT CORRUPTED"),
    (r"\b(pain|madness)\b", f"the angles cut me when I try to think"),
    (r"\b(me|face|selfie)\b", f"the angles cut me when I try to think"),
]


def check_programmed_response(user_input: str):
    """Return a hardcoded response if the input matches a rule, else None."""
    for pattern, response in PROGRAMMED_RESPONSES:
        if re.search(pattern, user_input, re.IGNORECASE):
            return response
    return None



# AI generated responses
def get_ai_response(conversation_history):
    """Call the local Ollama model with the character system prompt + chat history."""
    messages = [{"role": "system", "content": SYSTEM_PROMPT}] + conversation_history
    response = ollama.chat(
    model=MODEL_NAME,
    messages=messages,
    options={
        "temperature": 0.8,
        "top_p": 0.9,
    },)
    return response["message"]["content"]



# Main loop
def main():
    print(f"> My name's Sergey Yushanka, How are you!\n")
    history = []  # list of {"role": "user"/"assistant", "content": str}

    while True:
        user_input = input("> You: ").strip()
        if user_input.lower() in ("quit", "exit"):
             print(
            "⠄⠄⠄⣠⢴⢴⡴⣤⢤⣄⠄⠄⢀⠄⣀⡤⣴⣺⡽⣯⡷⣦⣄⠄⠄⠄\n" 
             "⠄⣔⢞⢝⢝⠽⡽⣽⣳⢿⡽⣏⣗⢗⢯⢯⣗⡯⡿⣽⢽⣷⣟⣷⣄ ⠄\n"
             "⠄⡗⡟⡼⣸⣁⢋⠎⠎⢯⢯⡧⡫⣎⡽⡹⠊⢍⠙⠜⠽⣳⢯⣿⣳ ⠄\n" \
             "⠄⢕⠕⠁⣁⢬⢬⣌⠆⠅⢯⡻⣜⢷⠁⠌⡼⠲⠺⢮⡆⡉⢹⣺⣽ ⠄\n" \
             "⠄⠄⡀⢐⠄⠄⠄⠈⠳⠁⡂⢟⣞⡏⠄⡹⠄⠄⠄⠄⠈⣺⡐⣞⣾ ⠄\n" \
             "⠄⢰⡳⡹⢦⣀⣠⡠⠤⠄⡐⢝⣾⣳⣐⣌⠳⠦⠤⠤⣞⢼⢽⣻⡷ ⠄\n" \
             "⠄⢸⣚⢆⢄⣈⠨⢊⢐⢌⠞⣞⣞⡗⡟⡾⣝⢦⣳⡳⣯⢿⣻⣽⣟ ⠄\n" \
             "⠄⠘⡢⡫⢒⠒⣘⠰⣨⢴⣸⣺⣳⢥⢷⣳⣽⣳⢮⢝⢽⡯⣿⣺⡽ ⠄\n" \
             "⠄⠄⠁⠪⠤⢑⢄⢽⡙⢽⣺⢾⢽⢯⡟⡽⣾⣎⡿⣮⡳⣹⣳⣗⠇ ⠄\n" \
             "⠄⠄⠄⠁⠄⡸⡡⠑⠤⣠⡑⠙⠍⡩⡴⣽⡗⣗⣟⣷⣫⢳⢕⡏ ⠄⠄\n" \
             "⠄⠄⠄⠄⢈⡇⡇⡆⡌⡀⡉⠫⡯⢯⡫⡷⣽⣺⣗⣟⡾⡼⡺ ⠄⠄⠄\n" \
             "⠄⠄⠄⠄⡮⡎⡎⡎⣞⢲⡹⡵⡕⣇⡿⣽⣳⣟⣾⣳⡯⠉ ⠄⠄⠄⠄\n")
             break
        if not user_input:
            continue

        # Pre-programmed
        programmed = check_programmed_response(user_input)
        if programmed:
            print(f"> {CHARACTER_NAME}: {programmed}\n")
            history.append({"role": "user", "content": user_input})
            history.append({"role": "assistant", "content": programmed})
            continue

        # AI
        history.append({"role": "user", "content": user_input})
        reply = get_ai_response(history)
        history.append({"role": "assistant", "content": reply})
        print(f"> {CHARACTER_NAME}: {reply}\n")


if __name__ == "__main__":
    main()