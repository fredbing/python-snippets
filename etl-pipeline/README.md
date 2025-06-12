<<<<<<< HEAD
# projects I developed

# datapipeline-python

=======
# dataPipeline-python
>>>>>>> 6937e934f099a11f4d40943b137c57aa641cc7c8
Building data pipelines with python scripts. 

### excel_csv_to_s3.py 

This script is for transforming and uploading a batch of historic files. The python script is written for modifying a series of existing excel xlsx worksheets, converting them to csv formats, and upload them to AWS S3.

In one application, there were a series of historic excel files having the same template but different values over time (e.g., for differen years). It required to add a new ID column to differntiate the data from different years. The modified excel files were converted to csv format and saved to a local directory (as references), and uploaded to AWS S3 with Boto3 API.

### lambda_s3_csv_dynamo.py 

This is a lambda function in python for loading the csv files to AWS DynamoDB once they are uploaded from local directory to AWS S3. Whenever there is an update (incremental change) of the csv files in S3, a CloudWatch event will trigger the lambda function to make the same update available at the DynamoDB table in real-time. 

### watch_dir.py

In case of upload real-time changes from local compater to S3, it needs to watch for the new events occured in the local file directory. When a file is saved with updates, it will generate a 'Modified event', which will make the os.system() method run the script to transform the file and send the updates to AWS S3.

### excel_realtime_to_s3.py

This script is witten for updating a file in local directory to AWS S3 in real-time.

An existing excel file in a local computer has frequent updates. The updates are required to be reflected in AWS S3 and DynamoDB in real-time. 

The updates are made in the excel file regularly , each time the excel file is saved with new updates, it is edited by adding a new ID column and converted to csv format. The updates are uploaded to S3 in real-time, and then sent to DynamoDB table by a lambda function triggerd by CloudWatch event.

