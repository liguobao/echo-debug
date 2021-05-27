# echo debug server

```sh

docker run -e API_ENTRY=http://192.168.31.135:4826/ -e CLIENT_ID=local_echo_client -e ECHO_ACCOUNT=admin -e ECHO_PASSWORD=admin --restart=always --name=local__debug_echo_client -d registry.cn-beijing.aliyuncs.com/virjar/echo-client


docker run -e API_ENTRY=http://192.168.31.135:4826/ -e CLIENT_ID=local_echo_client_2 -e ECHO_ACCOUNT=admin -e ECHO_PASSWORD=admin --restart=always --name=local__debug_echo_client_2 -d registry.cn-beijing.aliyuncs.com/virjar/echo-client


spring.datasource.username=root
spring.datasource.password=echo
spring.datasource.url=jdbc:mysql://127.0.0.1:4444/echo?useUnicode=true&characterEncoding=utf8&zeroDateTimeBehavior=convertToNull&useSSL=false&autoConnect=true
spring.datasource.driver-class-name=com.mysql.cj.jdbc.Driver


ENV API_ENTRY="http://echonew.virjar.com/"
ENV MAPPING_SERVER_URL="http://127.0.0.1:4826/echoNatApi/connectionList"
ENV MAPPING_SERVER_FORCE_HOST="127.0.0.1"
ENV AUTH_CONFIG_URL="http://127.0.0.1:4826/echoNatApi/syncAuthConfig"
ENV SERVER_ID="echo-http-proxy-001"
ENV MAPPING_SPACE="33001-34000"
ENTRYPOINT "/app/bin/EchoHttpServer.sh" \
    "--mapping-server-url" "${MAPPING_SERVER_URL}"  \
    "--auth-config-url" "${AUTH_CONFIG_URL}" \
    "--api-entry" "${API_ENTRY}" \
    "--mapping-space" "${MAPPING_SPACE}"

    --mapping-server-url http://127.0.0.1:4826/echoNatApi/connectionList --auth-config-url http://127.0.0.1:4826/echoNatApi/syncAuthConfig  --api-entry http://127.0.0.1:4826 --mapping-space 33001-32010




http://192.168.31.135:4826/echo-api/nat-mapping-server/sendCommandToClient?clientId=admin%7C%40--%40--%40%7Cunknown_8185&action=ShizukuReDial&additionParam=whoami&token=1b7ac4ae-cc5f-493a-bfed-f413d50c3011


http://192.168.31.135:4826/echo-api/nat-mapping-server/sendCommandToClient?clientId=admin%7C%40--%40--%40%7Cunknown_8185&action=ShizukuReDial&additionParam=whoami&token=1b7ac4ae-cc5f-493a-bfed-f413d50c3011

export https_proxy=http://10086:10086@192.168.31.135:35006;curl -vvv https://www.baidu.com

export https_proxy=http://10086:10086@aoba.vip:13006;curl -vvv https://www.baidu.com


http://192.168.31.135:4826/echo-api/nat-mapping-server/sendCommandToClient?clientId=admin%7C%40--%40--%40%7C865932025868934_47&action=ShizukuReDial&additionParam=whoami&token=cc37004a000d007c008b008700e600eeea800d053393ed07


http://aoba.vip:4826/echo-api/nat-mapping-server/sendCommandToClient?clientId=admin%7C%40--%40--%40%7C865932025868934_47&action=ShizukuReDial&additionParam=whoami&token=014a00eb002800fe00ac0042003100fa1dbe8adde382fdad

http://aoba.vip:4826/echo-api/nat-mapping-server/sendCommandToClient?clientId=admin%7C%40--%40--%40%7C353626072983559_1814&action=ShizukuReDial&additionParam=whoami&token=0197003f00c7001c00af00be00da009410c5ca7c25cfcf64


admin|@--@--@|353626072983559_1814

http://192.168.31.135:4826/echo-api/nat-mapping-server/sendCommandToClient?clientId=admin%7C%40--%40--%40%7C353626072983559_4791&action=ShizukuReDial&additionParam=whoami&token=cc37004a000d007c008b008700e600eeea800d053393ed07


export https_proxy=http://10086:10086@aoba.vip:13016;curl -vvv https://www.baidu.com
```