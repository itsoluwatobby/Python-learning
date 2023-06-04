from random import choice

capital = 'Ibadan'
bird = 'Western Meadowlark'
flower = 'Sunflower'
song = 'Home on the Range'

def randomFunFact():
    funFact = [
        "Lorem ipsum dolor sit amet consectetur adipisicing elit.", 
        "Excepturi est tempora nemo voluptatem qui voluptates autem accusantium dignissimos vitae repellendus maxime sapiente culpa officia.", 
        "sunt harum hic mollitia nihil officiis! Accusamus", 
        "doloribus maxime soluta dolore dolorum molestias dicta provident facilis dolor ipsa reprehenderit. Similique velit."
    ]
    index = choice("0123")
    print(f"{funFact[int(index)]}")

#if __name__ == "__main__":
randomFunFact()

