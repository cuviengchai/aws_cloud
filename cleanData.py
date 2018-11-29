def accumulateFile(folder, filename_list):
    output_list = dict()
    for file in filename_list:
        with open("Output/"+folder+"/"+file,'r') as f:
            data = json.load(f)
            key = data['jobName'].split('_')
        output_list[key[1]] = data['results']['transcripts'][0]['transcript']
    return output_list
 
filename_list = ['312.json',
'313.json',
'314.json',
'315.json',
'316.json',
'317.json',
'318.json',
'319.json',
'320.json',
'321.json',]
                 
                 
folder = 'male-other-01'


output = accumulateFile(folder,filename_list)
outputfile = "Sound/"+folder+"/etc/c_"+folder+".json"
with open(outputfile,'w+') as f:
    my_json = json.dumps(output)
    f.write(my_json)
# output
