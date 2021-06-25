import random


def mood_dict_engine(mood):

    mood_to_key = {
        "happy": ["C major", "A major", "Bb major"],
        "angry": ["D major", "D# minor", "Eb major", "E major", "B major"],
        "disgusted": ["F major", "F minor", "Ab minor"],
        "fearful": ["E minor", "G minor", "Ab major"],
        "neutral": ["A minor", "D minor", "G major", "B minor"],
        "sad": ["C minor", "C# minor", "Db major", "F# minor"],
        "surprised": ["F# major", "Bb minor"]
    }

    key_list = mood_to_key[mood]

    random_idx = random.randint(0, len(key_list)-1)

    return key_list[random_idx]

