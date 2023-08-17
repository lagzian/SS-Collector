import json
import base64
import os
import time

out_json = './out.json'

sub_all_base64 = "./sub/sub_merge_base64.txt"
sub_all = "./sub/sub_merge.txt"
Trinity_file_base64 = "./SS/Trinity"
Trinity_file = "./SS/Trinity.txt"
Trinity_Base = "./SS/TrinityBase"

splitted_output = "./sub/splitted/"

def read_json(file):
    while not os.path.isfile(file):
        print('Awaiting speedtest complete')
        time.sleep(30)
    with open(file, 'r', encoding='utf-8') as f:
        print('Reading out.json')
        proxies_all = json.load(f)["nodes"]
    return proxies_all

def output(list, num):
    def arred(x, n): return x * (10 ** n) // 1 / (10 ** n)
    output_list = []

    for item in list:
        info = "id: %s | remarks: %s | protocol: %s | ping: %s MS | avg_speed: %s MB | max_speed: %s MB | Link: %s\n" % (
            str(item["id"]), item["remarks"], item["protocol"], str(item["ping"]), str(arred(item["avg_speed"] * 0.00000095367432, 3)),
            str(arred(item["max_speed"] * 0.00000095367432, 3)), item["link"])
        output_list.append(info)

    with open('./LogInfo.txt', 'w') as f1:
        f1.writelines(output_list)
        print('Write Log Success!')

    output_list = [item["link"] for item in list]

    content = '\n'.join(output_list)
    content_base64 = base64.b64encode(content.encode('utf-8')).decode('ascii')
    content_base64_part = base64.b64encode('\n'.join(output_list[0:num]).encode('utf-8')).decode('ascii')

    os.makedirs(splitted_output, exist_ok=True)
    vmess_outputs = []
    vless_outputs = []
    trojan_outputs = []
    ssr_outputs = []
    ss_outputs = []

    for output in output_list:
        if not str(output).startswith(("vmess://", "vless://", "ssr://")):
            if str(output).startswith("trojan://"):
                trojan_outputs.append(output)
            elif str(output).startswith("ss://"):
                ss_outputs.append(output)

    with open(os.path.join(splitted_output, "trojan.txt"), 'w') as f:
        trojan_content = "\n".join(trojan_outputs)
        f.write(trojan_content)
        print('Write trojan splitted Success!')

    with open(os.path.join(splitted_output, "ss.txt"), 'w') as f:
        ss_content = "\n".join(ss_outputs)
        f.write(ss_content)
        print('Write ss splitted Success!')

    with open(sub_all_base64, 'w+', encoding='utf-8') as f:
        f.write(content_base64)
        print('Write All Base64 Success!')

    with open(Trinity_file_base64, 'w+', encoding='utf-8') as f:
        f.write(content_base64_part)
        print('Write Part Base64 Success!')

    with open(sub_all, 'w') as f:
        f.write(content)
        print('Write All Success!')

    with open(Trinity_Base, 'w') as f:
        f.write(content)
        print('Write Base Success!')

    with open(Trinity_file, 'w') as f:
        f.write('\n'.join(output_list[0:num]))
        print('Write Part Base Success!')

    return content

if __name__ == '__main__':
    num = 300
    value = read_json(out_json)
    output(value, value.__len__() if value.__len__() <= num else num)
