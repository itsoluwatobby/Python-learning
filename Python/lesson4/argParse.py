
def hello(name: str, lang: str):
  greetings = dict(
    English="Hello",
    Spanish="Hola",
    German="Hallo",
  )
  msg = f"{greetings[lang]} {name}"
  print(msg)

if __name__ == "__main__":
  import argparse

  parser = argparse.ArgumentParser(
      description = "Provides a personal greeting.",
  )
  parser.add_argument(
      "-n", "--name", metavar="name", required=True,
      help="The name of the person to greet"
  )
  parser.add_argument(
      "-l", "--language", metavar="language", required=True,
      help="The language to greet person in", 
      choices=["English", "Spanish", "German"]
  )
  args = parser.parse_args()
  hello(args.name, args.language)