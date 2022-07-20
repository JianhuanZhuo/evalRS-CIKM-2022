"""

    Sample script showing how to submit a prediction json file to the AWS bucket assigned to you for the challenge.
    Credentials are in your sign-up e-mail: please refer to the full project README for the exact format of the file
    and the naming convention you need to respect.

    Make sure to duplicate the .env.local file as an .env file in this folder, and fill it with the right values
    (or alternatively, set up the corresponding env variables).

    Required packages can be found in the requirements.txt file in this folder.

"""

import os
import boto3
from datetime import datetime
from dotenv import load_dotenv

def upload_submission(
        local_file: str,
        aws_access_key_id: str,
        aws_secret_access_key: str,
        participant_id: str,
        bucket_name: str,

):
    """

    :param local_file: local path, may be only the file name or a full path
    :param task: rec or cart
    :return:
    """

    print("Starting submission at {}...\n".format(datetime.utcnow()))
    # instantiate boto3 client
    s3_client = boto3.client(
        's3',
        aws_access_key_id=aws_access_key_id ,
        aws_secret_access_key=aws_secret_access_key,
        region_name='us-west-2'
    )
    s3_file_name = os.path.basename(local_file)
    # prepare s3 path according to the spec
    s3_file_path = '{}/{}'.format(participant_id, s3_file_name)  # it needs to be like e.g. "id/*.json"
    # upload file
    s3_client.upload_file(local_file, bucket_name, s3_file_path)
    # say bye
    print("\nAll done at {}: see you, space cowboy!".format(datetime.utcnow()))

    return


if __name__ == "__main__":
    # load envs from env file
    # load_dotenv(verbose=True, dotenv_path='upload.env')
    load_dotenv('./upload.env')
    # env info should be in your env file
    EMAIL = os.getenv('EMAIL')  # the e-mail you used to sign up
    BUCKET_NAME = os.getenv('BUCKET_NAME') # you received it in your e-mail
    PARTICIPANT_ID = os.getenv('PARTICIPANT_ID') # you received it in your e-mail
    AWS_ACCESS_KEY = os.getenv('AWS_ACCESS_KEY') # you received it in your e-mail
    AWS_SECRET_KEY = os.getenv('AWS_SECRET_KEY') # you received it in your e-mail

    # LOCAL_FILE needs to be a json file with the format email_epoch time in ms - email should replace @ with _
    # LOCAL_FILE = '{}_ts.json'.format(EMAIL.replace('@', '_'))
    LOCAL_FILE = "pchia_coveo.com_1657739234.980365.json"
    upload_submission(local_file=LOCAL_FILE,
                      aws_access_key_id=AWS_ACCESS_KEY,
                      aws_secret_access_key=AWS_SECRET_KEY,
                      participant_id=PARTICIPANT_ID,
                      bucket_name=BUCKET_NAME)
