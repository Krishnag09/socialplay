import random


def mood_dict_engine(mood):

    mood_to_key = {
        "happy": ["C major", "A major", "BB major"],
        "angry": ["D major", "D# minor", "EB major", "E major", "B major"],
        "disgusted": ["F major", "F minor", "AB minor"],
        "fearful": ["E minor", "G minor", "AB major"],
        "neutral": ["A minor", "D minor", "G major", "B minor"],
        "sad": ["C minor", "C# minor", "DB major", "F# minor"],
        "surprised": ["F# major", "BB minor"]
    }

    key_list = mood_to_key[mood]

    random_idx = random.randint(0, len(key_list)-1)

    return key_list[random_idx]

