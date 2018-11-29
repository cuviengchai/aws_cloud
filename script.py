from __future__ import print_function
import time
import boto3
import json

def process(folder, filename):
    transcribe = boto3.client('transcribe')
    job_name = folder+"_"+filename
    print(job_name)
    job_uri = "https://s3-ap-southeast-2.amazonaws.com/"+folder+"/"+filename
    transcribe.start_transcription_job(
        TranscriptionJobName=job_name,
        Media={'MediaFileUri': job_uri},
        MediaFormat='wav',
        LanguageCode='en-US'
    )
    while True:
        status = transcribe.get_transcription_job(TranscriptionJobName=job_name)
        if status['TranscriptionJob']['TranscriptionJobStatus'] in ['COMPLETED', 'FAILED']:
            break
        time.sleep(5)
    print(status['TranscriptionJob']['TranscriptionJobStatus'])
    return status['TranscriptionJob']
    
filename_list = #['b0074.wav','b0075.wav','b0076.wav','b0077.wav']
folder = #"female-american-02"
all = []
for i in filename_list:
    status = process(folder,i)
    if status["TranscriptionJobStatus"] == 'COMPLETED':
        mytime = status["CompletionTime"] - status["CreationTime"]
        all.append({i : (mytime.seconds, mytime.microseconds)})
    else:
        print ('Error file', i)
        break
