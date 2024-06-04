# Source Code for FunctionBench applications and micro-benchmarks developed for running a microservices on Kubernetes

All of the 10 tests have been adapted from the [kmu-bigdata/serverless-faas-workbench](https://github.com/ddps-lab/serverless-faas-workbench) repository.


# CPU-Memory

## 1. Image Processing
Added memory clean-up

### Build Function
sudo docker build -t image-processing-service .
sudo docker tag image-processing-service 192.168.56.10:5000/image-process
sudo docker push 192.168.56.10:5000/image-process

### Input Json
{"input_bucket": "picturesinput", "object_key": "input/input_sina.jpg", "output_bucket": "processedimages", "key_id": "cu7oaEMkZhQ6WXmouxYY", "access_key": "WmzOQrLaL6bwzlxJ5BZ8eU3twCLioqTGX6YgxQcx", "uuid": "1234"}

### Input Data
1,image-process,http://192.168.56.10:31461/process-image,input_bucket:picturesinput|object_key:input/input_sina.jpg|output_bucket:processedimages|key_id:cu7oaEMkZhQ6WXmouxYY|access_key:WmzOQrLaL6bwzlxJ5BZ8eU3twCLioqTGX6YgxQcx|uuid:1234,600,550

### Resources
not set

### HPA
Added

### Curl command
curl -X POST -H "Content-Type: application/json" -d '{"input_bucket": "picturesinput", "object_key": "input/input_sina.jpg", "output_bucket": "processedimages", "key_id": "cu7oaEMkZhQ6WXmouxYY", "access_key": "WmzOQrLaL6bwzlxJ5BZ8eU3twCLioqTGX6YgxQcx", "uuid": "1234"}' 192.168.56.10:31461/process-image

### Scale in/out
Tested

### Pull images on nodes
Not done.



## 2. Linpack
Added concurrency tracker, memory clean up

### Build function
sudo docker build -t linpack-service .
sudo docker tag linpack-service 192.168.56.10:5000/linpack-image
sudo docker push 192.168.56.10:5000/linpack-image


### Input Json
{"number": "picturesinput", "uuid": "1234"}

## Input data
1,linpack,http://192.168.56.10:31147/linpack,number:50|uuid:1234,600,550

### Resources
not set

### HPA
Scale in/out tested

### Curl command
curl -X POST -H "Content-Type: application/json" -d '{"number": 10, "uuid": "1234"}' 192.168.56.10:32568/linpack

### Pull images on nodes
Note done.


## 3. Chameleon
Added concurrency tracker, memory clean up

### Build function
sudo docker build -t chameleon .
sudo docker tag chameleon 192.168.56.10:5000/chameleon
sudo docker push 192.168.56.10:5000/chameleon


### Input Json
{"num_of_rows": 10, "num_of_cols": 10, "uuid": "1234"}

### Input data
1,chameleon,http://192.168.56.10:32568/generate_table,num_of_rows:10|num_of_cols:10|uuid:1234,600,550

### Resources
not set

### HPA
Scale in/out tested

### Curl command
curl -X POST -H "Content-Type: application/json" -d '{"num_of_rows": 10, "num_of_cols": 10, "uuid": "1234"}' 192.168.56.10:32568/generate_table

### Pull images on nodes
Note done.


## 4. matmul

### Build function
sudo docker build -t matmul . 
sudo docker tag matmul 192.168.56.10:5000/matmul
sudo docker push 192.168.56.10:5000/matmul

### Input Json
{"number": 500, "uuid": "1234"}

### Input Data
1,matmul,http://192.168.56.10:32418/matmul,number:500|uuid:1234,600,550

### Resources
not set

### HPA
Scale in/out tested

### Curl Command
curl -X POST -H "Content-Type: application/json" -d '{"number": 500, "uuid": "1234"}' 192.168.56.10:1234/matmul

### Pull images on nodes
Not done yet.

## 5. Float-operations

### Build function
sudo docker build -t float-operations-image . 
sudo docker tag float-operations-image 192.168.56.10:5000/float-operations-image
sudo docker push 192.168.56.10:5000/float-operations-image

### Input Json
{"number": 500, "uuid": "1234"}

### Input Data
1,float,http://192.168.56.10:31976/float-operations,number:500|uuid:1234,600,550

### Resources
not set

### HPA


### Curl Command
curl -X POST -H "Content-Type: application/json" -d '{"number": 500, "uuid": "1234"}' 192.168.56.10:31976/float-operations

### Pull images on nodes
Not done yet.


## 6. Pyaes

### Build function
sudo docker build -t pyaes-image . 
sudo docker tag pyaes-image 192.168.56.10:5000/pyaes-image
sudo docker push 192.168.56.10:5000/pyaes-image

### Input Json
{"length_of_message": 100, "num_of_iterations": 10, "uuid": "1234"}

### Input Data
1,float,http://192.168.56.10:30538/pyaes,length_of_message:100|num_of_iterations:10|uuid:1234,600,550

### Resources
not set

### HPA
scale in/out tested

### Curl Command
curl -X POST -H "Content-Type: application/json" -d '{"length_of_message": 100, "num_of_iterations": 10, "uuid": "1234"}' 192.168.56.10:/pyaes-image

### Pull images on nodes
Not done yet.

# Disk

## 7. dd

### Build function
sudo docker build -t dd-image . 
sudo docker tag dd-image 192.168.56.10:5000/dd-image
sudo docker push 192.168.56.10:5000/dd-image

### Input Json
{"bs": 1024, "count": 5, "uuid": "1234"}

### Input Data
1,dd,http://192.168.56.10:31966/io-operation,bs:1024|count:5|uuid:1234,600,550

### Resources
not set

### HPA
scale in/out tested

### Curl Command
curl -X POST -H "Content-Type: application/json" -d '{"bs": 1024, "count": 5, "uuid": "1234"}' 192.168.56.10:31966/io-operation

### Pull images on nodes
Not done yet.

## 8. gzip compression

### Build function
sudo docker build -t gzip-image . 
sudo docker tag dd-image 192.168.56.10:5000/gzip-image
sudo docker push 192.168.56.10:5000/gzip-image

### Input Json
{"file_size": 1, "uuid": "1234"}

### Input Data
1,gzip,http://192.168.56.10:31954/compress-file,file_size:1|uuid:1234,600,550

### Resources
not set

### HPA
scale in/out tested

### Curl Command
curl -X POST -H "Content-Type: application/json" -d '{"file_size": 1, "uuid": "1234"}' 192.168.56.10:31954/compress-file

### Pull images on nodes
Not done yet.

# Network

## 9. Json

### Build function
sudo docker build -t json-image . 
sudo docker tag json-image 192.168.56.10:5000/json-image
sudo docker push 192.168.56.10:5000/json-image

### Input Json
{"link": "http://api.worldbank.org/v2/countries/USA/indicators/NY.GDP.MKTP.CD?per_page=5000&format=json", "uuid": "1234"}

### Input Data
1,json,http://192.168.56.10:30888/json-dumps-loads,link:api.worldbank.org/v2/countries/USA/indicators/NY.GDP.MKTP.CD?per_page=5000&format=json|uuid:1234,600,550

### Resources
not set

### HPA
scale in/out tested

### Curl Command
curl -X POST -H "Content-Type: application/json" -d '{"link": "http://api.worldbank.org/v2/countries/USA/indicators/NY.GDP.MKTP.CD?per_page=5000&format=json", "uuid": "1234"}' 192.168.56.10:30888/json-dumps-loads

### Pull images on nodes
Not done yet.


## 10. S3 download speed

### Build function
sudo docker build -t s3-image . 
sudo docker tag s3-image 192.168.56.10:5000/s3-image
sudo docker push 192.168.56.10:5000/s3-image

### Input Json
{"input_bucket": "vidsbucket", "object_key": "input/vids", "output_bucket": "downloadedvids", "key_id": "cu7oaEMkZhQ6WXmouxYY", "access_key": "WmzOQrLaL6bwzlxJ5BZ8eU3twCLioqTGX6YgxQcx", "uuid": "1234"}

### Input Data
1,s3,http://192.168.56.10:32727/s3-operation,input_bucket:vidsbucket|object_key:input/vids|output_bucket:downloadedvids|key_id:cu7oaEMkZhQ6WXmouxYY|access_key:WmzOQrLaL6bwzlxJ5BZ8eU3twCLioqTGX6YgxQcx|uuid:1234,600,550

### Resources
not set

### HPA
scale in/out tested

### Curl Command
curl -X POST -H "Content-Type: application/json" -d '{"input_bucket": "vidsbucket", "object_key": "input/vids", "output_bucket": "downloadedvids", "key_id": "cu7oaEMkZhQ6WXmouxYY", "access_key": "WmzOQrLaL6bwzlxJ5BZ8eU3twCLioqTGX6YgxQcx", "uuid": "1234"}' 192.168.56.10:32727/s3-operation


### Pull images on nodes
Not done yet.


