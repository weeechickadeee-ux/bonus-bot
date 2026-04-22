from processor.video import process_video
from processor.text import process_text

async def handle_message(msg):

    # VIDEO PATH
    if msg.video:
        print("Video detected")
        file_path = await msg.download_media()
        code = process_video(file_path)

    # TEXT PATH
    else:
        print("Text detected")
        code = process_text(msg.message)

    if code:
        print("Code extracted:", code)
        from web.submit import submit_code
        submit_code(code)