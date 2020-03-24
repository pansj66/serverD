import sys
import os

from conf import *

file_path = os.path.abspath(os.path.dirname(__file__))

class ServerD:

    @staticmethod
    def serverB(s_type, s_data):
        cmd = '{}/serverE/{} {}'.format(file_path, s_type, s_data)
        print(cmd)
        os.system(cmd)

    def login(self, server_name):
        s_type = "serverLogin"
        if not isinstance(server_name, str):
            server_name = "{}".format(server_name)
        login_dict = server_dict.get(server_name)
        if not login_dict:
            print("{} 不存在".format(server_name))
            exit(1)
        s_data = server_base_data.get(s_type).format(**login_dict)
        self.serverB(s_type, s_data)

    def get(self, server_name, locPath, serPath):
        s_type = "serverGet"
        if not isinstance(server_name, str):
            server_name = "{}".format(server_name)
        get_dict = server_dict.get(server_name)
        if not get_dict:
            print("{} 不存在".format(server_name))
            exit(1)
        get_dict.update({"locPath": locPath, "serPath": serPath})
        s_data = server_base_data.get(s_type).format(**get_dict)
        self.serverB(s_type, s_data)

    def put(self, server_name, locPath, serPath):
        s_type = "serverPut"
        if not isinstance(server_name, str):
            server_name = "{}".format(server_name)
        get_dict = server_dict.get(server_name)
        if not get_dict:
            print("{} 不存在".format(server_name))
            exit(1)
        get_dict.update({"locPath": locPath, "serPath": serPath})
        s_data = server_base_data.get(s_type).format(**get_dict)
        self.serverB(s_type, s_data)

    def loginRoot(self, server_name):
        s_type = "serverLogin"
        if not isinstance(server_name, str):
            server_name = "{}".format(server_name)
        login_dict = server_dict.get(server_name)
        if not login_dict:
            print("{} 不存在".format(server_name))
            exit(1)
        login_dict["user"] = "root"
        login_dict["pwd"] = root_pwd
        s_data = server_base_data.get(s_type).format(**login_dict)
        self.serverB(s_type, s_data)

    def loginTbj(self, pwd):
        """
        :param server_name:
        :return:
        """
        s_type = "serverTbj"
        login_dict = server_dict.get("tbj")
        login_dict["pwd"] = pwd
        s_data = server_base_data.get(s_type).format(**login_dict)
        self.serverB(s_type, s_data)

    def main(self, server):
        try:
            if server:
                if server == "tbj":
                    try:
                        self.loginTbj(sys.argv[2])
                    except IndexError:
                        print("请输入正确格式: go tbj password")
                elif server == "root":
                    try:
                        self.loginRoot(sys.argv[2])
                    except IndexError:
                        print("请输入正确格式 go root server: 如: go root 429")

                elif server == "get":
                    try:
                        server_name = sys.argv[2]
                        serPath = sys.argv[3]
                        locPath = sys.argv[4]
                        self.get(server_name, locPath, serPath)
                    except IndexError:
                        print("输入参数错误!!!\n正确示例 >>> go get <服务器名称> <服务器文件路径> <本地文件路径>")

                elif server == "put":
                    try:
                        server_name = sys.argv[2]
                        serPath = sys.argv[3]
                        locPath = sys.argv[4]
                        self.put(server_name, locPath, serPath)
                    except IndexError:
                        print("输入参数错误!!!\n正确示例 >>> go put <服务器名称> <服务器文件路径> <本地文件路径>")

                else:
                    server_name = "{}".format(server)
                    print("正在登录{}...".format(server_name))
                    self.login(server_name)
            else:
                print("请输入服务器编号")
        except IndexError:
            print("输入参数错误!!!\n正确示例 >>>  go [] <服务器名称> ")


def main():
    base_server = sys.argv[1]
    sd = ServerD()
    sd.main(base_server)


if __name__ == '__main__':
    main()