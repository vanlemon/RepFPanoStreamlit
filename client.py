import os
import time
import platform
import subprocess

import grpc
import proto_gen.detect_pb2
import proto_gen.detect_pb2_grpc

def write_log(log_path: str, line: str):
    log = open(log_path, "a")
    log.write(line)
    log.write('\n')
    log.close()



def detect_client(image_path):
    repf_pano_client(image_path)
    # example_client(image_path)


def repf_pano_client(image_path):
    with grpc.insecure_channel('localhost:50052') as channel:
        stub = proto_gen.detect_pb2_grpc.DeformYolov5Stub(channel)

        response = stub.Detect(
            proto_gen.detect_pb2.YoloModelRequest(
                image_path=image_path,
            ),
        )

        print("Greeter client received: ")
        print(response)

    deep_work_dir = f'{image_path}.deep'  # image save work dir
    if not os.path.exists(deep_work_dir):
        os.makedirs(deep_work_dir)
        os.makedirs(f'{deep_work_dir}/input')
    
    #sub = subprocess.Popen(f"./repf_pano_client.sh {image_path[:-9]}", shell=True, stdout=subprocess.PIPE)
    #sub.wait()

    print(image_path)
    write_log(f'{image_path}.log', "scene.glb")

def example_client(image_path):
    image_path_list = image_path.split('\\')
    image_name = image_path_list[len(image_path_list) - 1]
    log_path = f'./{image_name}.log'

    sys = platform.system()
    if sys == 'Darwin':
        example = open("./example.log", "r")
    elif sys == 'Linux':
        example = open("./example.log.lab724", "r")
    else:
        print(f"Example Client do not support {sys} system")
        exit(255)

    for line in example:
        time.sleep(0.5)
        log = open(log_path, "a")
        log.write(line)
        log.close()
    example.close()


if __name__ == '__main__':
    example_client('./test.png')
