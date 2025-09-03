from flask import Flask, request, jsonify
import instaloader

app = Flask(__name__)
L = instaloader.Instaloader()

@app.route("/", methods=["GET"])
def index():
    return "Instagram Video Downloader API is running. Use POST /get_video_link with JSON {'url': '<Instagram URL>'}."


@app.route('/get_video_link', methods=['POST'])
def get_video_link():
    data = request.get_json()
    url = data.get("url")
    
    if not url:
        return jsonify({"status": "error", "message": "No URL provided"})
    
    try:
        # Determine shortcode from URL
        if "/p/" in url:
            shortcode = url.split("/p/")[1].split("/")[0]
        elif "/reel/" in url:
            shortcode = url.split("/reel/")[1].split("/")[0]
        else:
            return jsonify({"status": "error", "message": "Invalid Instagram URL"})
        
        # Fetch post
        post = instaloader.Post.from_shortcode(L.context, shortcode)
        
        # Check if it's a video
        if post.is_video:
            return jsonify({"status": "success", "mp4_link": post.video_url})
        else:
            return jsonify({"status": "error", "message": "Post is not a video"})
    
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)})

if __name__ == '__main__':
    app.run(port=5000)
