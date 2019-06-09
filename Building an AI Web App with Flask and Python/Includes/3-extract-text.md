# Use Azure Cognitive Services to extract text from photos

TODO: Add introduction.

## Get a Computer Vision API key

TODO: Add intro.

1. tk.

1. tk.

1. tk.

TODO: Add closing.

## Modify the site to use the Computer Vision API

TODO: Add intro.

1. Open **app.py** and replace its contents with the following:

	```python
	import os, base64
	from flask import Flask, render_template, request, flash
	
	from azure.cognitiveservices.vision.computervision import ComputerVisionClient
	from azure.cognitiveservices.vision.computervision.models import ComputerVisionErrorException
	from msrest.authentication import CognitiveServicesCredentials
	
	# Create a ComputerVisionClient for calling the Computer Vision API
	vision_key = os.environ["VISION_KEY"]
	vision_endpoint = os.environ["VISION_ENDPOINT"]
	vision_credentials = CognitiveServicesCredentials(vision_key)
	vision_client = ComputerVisionClient(vision_endpoint, vision_credentials)
	
	app = Flask(__name__)
	app.secret_key = os.urandom(24)
	
	@app.route("/", methods=["GET", "POST"])
	def index():
	    if request.method == "POST":
	        # Display the image that was uploaded
	        image = request.files["file"]
	        uri = "data:image/jpg;base64," + base64.b64encode(image.read()).decode("utf-8")
	        image.seek(0)
	
	        # Use the Computer Vision API to extract text from the image
	        lines = extract_text_from_image(image, vision_client)
	        
	        # Flash the extracted text
	        for line in lines:
	            flash(line)
	
	    else:
	        # Display a placeholder image
	        uri = "/static/placeholder.png"
	
	    return render_template("index.html", image_uri=uri)
	
	# Function that extracts text from images
	def extract_text_from_image(image, client):
	    try:
	        result = client.recognize_printed_text_in_stream(image=image)
	        lines=[]
	
	        if len(result.regions) == 0:
	            lines.append("Photo contains no text to translate")
	
	        else:
	            for line in result.regions[0].lines:
	                text = " ".join([word.text for word in line.words])
	                lines.append(text)
	
	        return lines
	
	    except ComputerVisionErrorException as e:
	        return ["Computer Vision API error: " + e.message]
	
	    except:
	        return ["Error calling the Computer Vision API"]
	```

	TODO: Explain this code.

1. Now open **index.html** and insert the following code and markup before the `<script>` element at the bottom of the page:

	```html
	<div class="container">	
	    <div class="row">
	        <div id="myModal" class="modal fade" role="dialog">
	            <div class="modal-dialog">
	                <div class="modal-content">
	                    <div class="modal-header">
	                        <button type="button" class="close" data-dismiss="modal">&times;</button>
	                        <h4 class="modal-title">Result</h4>
	                    </div>
	                    <div class="modal-body"></div>
	                </div>
	            </div>
	        </div>
	    </div>
	</div>

	{% with messages = get_flashed_messages() %}
	    {% if messages %}
	        <script type="text/javascript">
	            // If flash messages are queued up, show them in a modal dialog
	            var messages = {{ messages | safe }};
	            body = $(".modal-body");
	            body.empty();
	
	            for (i=0; i<messages.length; i++) {
	                body.append("<h2>" +  messages[i] + "</h2>");
	            }
	            
	            $("#myModal").modal("show");
	        </script>
	    {% endif %}
	{% endwith %} 
	```

	TODO: Explain this code.

Finish up by saving your changes to **index.html** and **app.py**.

## Extract text from photos

Now let's run the modified site, upload a few photos, and see if the Computer Vision API lives up to its billing.

1. If you are running Windows, execute the following commands to create environment variables containing the API key and endpoint you retrieved for the Computer Vision API, replacing `computer_vision_api_key` with the API key and `computer_vision_endpoint` with the endpoint URL:

	```
	set VISION_KEY=computer_vision_api_key
	set VISION_ENDPOINT=computer_vision_endpoint
	```

	If you are running Linux or macOS, use these commands instead:

	```
	export VISION_KEY=computer_vision_api_key
	export VISION_ENDPOINT=computer_vision_endpoint
	```

	When the site is running locally, calls to `os.environ` in your Python code load these variables from the environment. Later, when you deploy the site to Azure, the same variables will come from application settings in Azure — no code changes required.

1. Navigate to http://localhost:5000 in your browser. Click the **Upload Photo** and button and upload a picture that contains text. Confirm that after a brief pause, the text extracted from the photo appears in a modal dialog. Then dismiss the dialog.

	![Translating text from a photo](media/extracted-text.png)

	_Translating text from a photo_

Repeat this process with other photos to gauge the Computer Vision API's ability to extract text from the photos you upload. It isn't perfect, but it should get it right — or almost right — most of the time.