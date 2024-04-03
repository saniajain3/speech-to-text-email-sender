# speech-to-text-email-sender
simple implementation of voice-controlled email sending functionality using Python.

# Voice-Controlled Email Sender

This Python script enables users to send emails using voice commands. It utilizes various libraries such as `smtplib`, `pyaudio`, `speech_recognition`, and `pyttsx3` to achieve voice input, text-to-speech output, and email sending functionality.

## Features

- **Voice Input**: Users can speak commands to specify the recipient's name, email subject, and body content.
- **Text-to-Speech Output**: Provides auditory feedback to the user using the `pyttsx3` library.
- **Email Sending**: Utilizes SMTP (Simple Mail Transfer Protocol) via the `smtplib` library to send emails.
- **Predefined Contacts**: Users can configure a dictionary mapping names to email addresses for quick access to contacts.

## Dependencies

- `smtplib`: For sending emails using SMTP.
- `pyaudio`: For audio input/output functionalities.
- `speech_recognition`: For converting speech to text.
- `pyttsx3`: For converting text to speech.

## Usage

1. Make sure you have the required dependencies installed. You can install them via pip:

2. Configure your Gmail account credentials in the `send_mail()` function.

3. Update the `dict` dictionary with the names and corresponding email addresses of your contacts.

4. Run the script and follow the voice prompts to send an email.

5. When the voice prompt says "Whom do you want to send the email to" say "test".

## Example

$ python email_sender.py
Talk
Recipient's name: "John Doe"
Talk
Email subject: "Meeting Agenda"
Talk
Email body: "Hi John, here's the agenda for our meeting tomorrow..."
Email sent successfully


## Limitations

- Currently only supports Gmail SMTP server. For other email providers, additional configurations may be required.
- Limited error handling and validation. Ensure correct input to avoid unexpected behavior.

## Contributors

- Sania jain

## License

This project is licensed under the [MIT License](LICENSE).
