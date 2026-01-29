sent_message = 'Hey there! This is a secret message.'

with open('sent_message.txt', 'w') as file:
  file.write(sent_message)

with open('sent_message.txt', 'r+') as file:
  # Read the sent message from the file
  original_message = file.read()
  print(original_message)
  # Move the cursor to the beginning of the file
  file.seek(0)

  # Modify the message to simulate unsending
  unsent_message = 'This message has been unsent.'
  file.write(unsent_message)

  # use truncate to reset the content to the length of the unsent message
  file.truncate(len(unsent_message))
  file.seek(0)
  print(file.read())
  print(f"The original message: {original_message}")
  print(f"The unsent message: {unsent_message}")