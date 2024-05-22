bucketName=$1
tableName=$2
region=$3

echo "Parameters $bucketName $tableName $region"
bucketstatus=$(aws s3api head-bucket --bucket $bucketName --region $region 2>&1)
echo "Existing Bucket status = $bucketstatus"
if [[ "$bucketstatus" =~ "Not Found" || "$bucketstatus" =~ "Forbidden" ]];
# if echo "$bucketstatus" | grep -q 'Not Found' || grep -q 'Forbidden';
then
  if [ $region = "us-east-1" ];
  then
    echo "IF BLOCK"
    bucket=$(aws s3api create-bucket --bucket $bucketName --region $region 2>&1)
  else
    echo "ELSE BLOCK"
    bucket=$(aws s3api create-bucket --bucket $bucketName --region $region --create-bucket-configuration LocationConstraint=$region 2>&1)
  fi
  echo "New Bucket Created: $bucket";
fi

tablestatus=$(aws dynamodb describe-table --table-name $tableName --region $region 2>&1)
echo "Existing Table status = $tablestatus"
if echo "${tablestatus}" | grep -q 'not found';
then
  table=$(aws dynamodb create-table --table-name $tableName --attribute-definitions AttributeName=LockID,AttributeType=S --key-schema AttributeName=LockID,KeyType=HASH --provisioned-throughput ReadCapacityUnits=5,WriteCapacityUnits=5 --region $region 2>&1)
  echo "New table created : $table";
fi