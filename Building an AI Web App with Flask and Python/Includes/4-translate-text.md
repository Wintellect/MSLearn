# Use Azure Cognitive Services to translate text

TODO: Add introduction.

## Get a Translator Text API key

TODO: Add intro.

1. tk.

1. tk.

1. tk.

TODO: Add closing.

## Modify the site to use the Translator Text API

TODO: Add intro.

1. Open **index.html** and tk:

	```html
	<select id="language" class="form-control" name="language">
	    <option value="en">English</option>
	    <option value="zh-Hant">Chinese (simplified)</option>
	    <option value="zh-Hans">Chinese (traditional)</option> 
	    <option value="fr">French</option>
	    <option value="de">German</option>
	    <option value="it">Italian</option>
	    <option value="ja">Japanese</option>
	    <option value="ko">Korean</option>
	    <option value="pt">Portugese</option>
	    <option value="es">Spanish</option>
	</select>
	```

	TODO: Explain this code.

1. Also in **index.html**, add the following statement to the `<script>` block at the bottom of the page:

	```javascript
	$("#language").val("{{ language }}");
	```

	Here's how the modified `<script>` block should look:

	```javascript
	<script type="text/javascript">
	    $(function() {
	        $("#upload-button").click(function() {
	            $("#upload-file").click();
	        });
	
	        $("#upload-file").change(function() {
	            $("#submit-button").click();
	        });
	
	        $("#language").val("{{ language }}");
	    });
	</script>
	```

	TODO: Explain this code.

1. Open **app.py** and replace its contents with the following:

	```python
	import os, base64, json, requests
	from flask import Flask, render_template, request, flash
	
	from azure.cognitiveservices.vision.computervision import ComputerVisionClient
	from azure.cognitiveservices.vision.computervision.models import ComputerVisionErrorException
	from msrest.authentication import CognitiveServicesCredentials
	
	# Create a ComputerVisionClient for calling the Computer Vision API
	vision_key = os.environ["VISION_KEY"]
	vision_endpoint = os.environ["VISION_ENDPOINT"]
	vision_credentials = CognitiveServicesCredentials(vision_key)
	vision_client = ComputerVisionClient(vision_endpoint, vision_credentials)
	
	# Retrieve the Translator Text API key 
	translate_key = os.environ["TRANSLATE_KEY"]
	
	app = Flask(__name__)
	app.secret_key = os.urandom(24)
	
	@app.route("/", methods=["GET", "POST"])
	def index():
	    language="en"
	
	    if request.method == "POST":
	        # Display the image that was uploaded
	        image = request.files["file"]
	        uri = "data:image/jpg;base64," + base64.b64encode(image.read()).decode("utf-8")
	        image.seek(0)
	
	        # Use the Computer Vision API to extract text from the image
	        lines = extract_text_from_image(image, vision_client)
	        
	        # Use the Translator Text API to translate text extracted from the image
	        language = request.form["language"]
	        translated_lines = translate_text(lines, language, translate_key)
	
	        # Flash the translated text
	        for translated_line in translated_lines:
	            flash(translated_line)
	
	    else:
	        # Display a placeholder image
	        uri = "/static/placeholder.png"
	
	    return render_template("index.html", image_uri=uri, language=language)
	
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
	
	# Function the translates text into the specified language
	def translate_text(lines, language, key):
	    uri = "https://api.cognitive.microsofttranslator.com/translate?api-version=3.0&to=" + language
	
	    headers = {
	        'Ocp-Apim-Subscription-Key': key,
	        'Content-type': 'application/json'
	    }
	
	    input=[]
	
	    for line in lines:
	        input.append({ "text": line })
	
	    try:
	        response = requests.post(uri, headers=headers, json=input)
	        response.raise_for_status() # Raise exception if call failed
	        results = response.json()
	
	        translated_lines = []
	
	        for result in results:
	            for translated_line in result["translations"]:
	                translated_lines.append(translated_line["text"])
	
	        return translated_lines
	
	    except requests.exceptions.HTTPError as e:
	        return ["Error calling the Translator Text API: " + e.strerror]
	
	    except Exception as e:
	        return ["Error calling the Translator Text API"]
	```

	TODO: Explain this code.

1. tk.

TODO: Add closing.

## Translate text extracted from photos

TODO: Add intro.

1. If you are running Windows, use the following command to create an environment variable containing the API key you retrieved for the Translator Text API, replacing `translator_text_api_key` with the API key:

	```
	set TRANSLATE_KEY=translator_text_api_key
	```

	If you are running Linux or macOS, use this command instead:

	```
	export TRANSLATE_KEY=translator_text_api_key
	```

1. Navigate to http://localhost:5000 in your browser. Confirm that the page now contains a drop-down list for selecting a language, as pictured below.

	![Selecting a language](media/select-language.png)

	_Selecting a language_

1. Select the language that you want to translate text into from the drop-down list. Then click the **Upload Photo** and button and upload a picture that contains text.

1. Confirm that after a brief pause, the text extracted from the photo and translated into the language you specified appears in a modal dialog. Then dismiss the dialog.

	![Extracing text from a photo](media/translated-text.png)

	_Extracing text from a photo_

Repeat this process with other photos to gauge the Translator Text API's ability to translate text you submit to it.