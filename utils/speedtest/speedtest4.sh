#准备好所需文件
wget -O lite-linux-amd64.gz https://github.com/xxf098/LiteSpeedTest/releases/download/v0.15.0/lite-linux-amd64-v0.15.0.gz
gzip -d lite-linux-amd64.gz
wget -O lite_config2.json https://raw.githubusercontent.com/lagzian/SS-Collector/main/utils/speedtest/lite_config3.json
#运行 LiteSpeedTest
chmod +x ./lite-linux-amd64
sudo nohup ./lite-linux-amd64 --config ./lite_config3.json --test https://raw.githubusercontent.com/lagzian/SS-Collector/refs/heads/main/VLESS/vless_vip.txt
