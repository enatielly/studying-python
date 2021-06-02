from ibm_watson import SpeechToTextV1
import json
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator

#API informations available on IBM Clound Services
url_s2t = "https://api.eu-gb.speech-to-text.watson.cloud.ibm.com/instances/41136b7b-778c-4905-86e7-02a90bb13fe8"
iam_apikey_s2t = "o8URZAFvfEYjYIG1pe5XpuJ379DkhaV9uu298IADr7Fy"

authenticator = IAMAuthenticator(iam_apikey_s2t)
s2t = SpeechToTextV1(authenticator=authenticator)
s2t.set_service_url(url_s2t)
s2t

#Download the audio file that use to convert into text
#wget -O PolynomialRegressionandPipelines.mp3  https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0101EN-SkillsNetwork/labs/Module%205/data/PolynomialRegressionandPipelines.mp3
#executar comando wget assim como comando pip no terminal integrado a pasta venv

#Path of the .wav file we would like to convert to text

filename='PolynomialRegressionandPipelines.mp3' #Uma vez baixado atraves do comando wget, trazer o arquivo para fora da pasta venv
with open(filename, mode='rb') as wav:
    response = s2t.recognize(audio=wav, content_type='audio/mp3')


#The attribute result contains a dictionary that includes the translation:
response.result
from pandas import json_normalize
json_normalize(response.result['results'], 'alternatives')
response

#obtain the recognized text and assign it to the variable recognized_text
recognized_text=response.result['results'][0]["alternatives"][0]["transcript"]
type(recognized_text)

#Language Translator
from ibm_watson import LanguageTranslatorV3


#API informations available on IBM Clound Services
url_lt='https://api.us-south.language-translator.watson.cloud.ibm.com/instances/5b10b0bf-d273-4ea9-8615-e73a352be4aa'
apikey_lt='MtVVJVAW8kn8SEvifm6AE0gc5HLKz6iLiXgAiIbJWOvL'

#current version of Language Translator, 2018-05-01
version_lt='2018-05-01'

# create a Language Translator object language_translator:
authenticator = IAMAuthenticator(apikey_lt)
language_translator = LanguageTranslatorV3(version=version_lt,authenticator=authenticator)
language_translator.set_service_url(url_lt)
language_translator

#Can get a Lists the languages that the service can identify > returns the language code
from pandas import json_normalize
json_normalize(language_translator.list_identifiable_languages().get_result(),'languages')

#Use method translate english to portuguese (Brazil)

#translation_response = language_translator.translate(\
#    text=recognized_text, model_id='en-es')
#translation_response

translation_response = language_translator.translate(\
    text=recognized_text, model_id='en-ptbr')
translation_response

#The result is a dictionary:
translation=translation_response.get_result()
translation

#Obtain the actual translation as a string as follows:
brazilian_translation =translation['translations'][0]['translation']
brazilian_translation

