MAX_CHUNK_TOKENS = 410   
EMBEDDER_LIMIT = 400    

def chunk(text:str, size=MAX_CHUNK_TOKENS)->list[str]:
    words = text.split()    # pretend 1 word = 1 token
    return [" ".join(words[i:i + size]) for i in range(0, len(words), size)]

def embed(chunk_text: list[str])->dict:
    if MAX_CHUNK_TOKENS <= EMBEDDER_LIMIT:
        words = chunk_text.split()
        kept = words
        return {"kept": len(kept), "lost": len(words) - len(kept)}
    else:
        return

if __name__ == "__main__":
    text = " ".join(f"w{i}" for i in range(1000))
    # print(f"Text = {text}  \n End")
    # print(chunk(text)[0])
    # print(embed(chunk_text=chunk(text)[0]))
    try :
        total_lost = sum(embed(c)["lost"] for c in chunk(text))
        print("words lost:", total_lost)
    except (TypeError, NameError) as e:
    # If something goes wrong, this block runs instead of crashing
        print(f"Cannot carry on. Error: {e}")
    