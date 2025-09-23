# Write a function taking in a string like WOW this is REALLY          amazing and returning Wow this is really amazing. String should be capitalized and properly spaced.
#
# Examples:
#
# "HELLO CAN YOU HEAR ME" --> "Hello can you hear me"
# "now THIS is REALLY interesting" --> "Now this is really interesting"
# "THAT was EXTRAORDINARY!" --> "That was extraordinary!"

def filter_words(st):
    result = []
    for i in st.split():
        if i.strip() != "":
            result.append(i)
    return ' '.join(result).lower().capitalize()