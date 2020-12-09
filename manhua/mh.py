'''
Author: your name
Date: 2020-11-24 21:55:24
LastEditTime: 2020-11-24 23:19:04
LastEditors: Please set LastEditors
Description: In User Settings Edit
FilePath: \.git\vscode\manhua\mh.py


图像识别组合API
'''
'''{'refresh_token': '25.9b1fdc9fd159a64b1028d314772be67c.315360000.1921588896.282335-23036717', 'expires_in': 2592000, 'session_key': '9mzdX7nkzi1lGV1xz3dewT5bsiyIwstXwc63gMjxNoMwUOhw1DWKESW/suEddqVyHnjiRwMpmBlU/3ZTpbbWyZWJNl92jQ==', 'access_token': '24.dc797f607a0e3d7b4b7dcd40e291955b.2592000.1608820896.282335-23036717', 'scope': 'public brain_all_scope brain_colourize brain_stretch_restore brain_dehaze brain_contrast_enhance brain_image_quality_enhance brain_style_trans brain_inpainting brain_image_definition_enhance brain_selfie_anime wise_adapt lebo_resource_base lightservice_public hetu_basic lightcms_map_poi kaidian_kaidian ApsMisTest_Test权限 vis-classify_flower lpq_开放 cop_helloScope ApsMis_fangdi_permission smartapp_snsapi_base smartapp_mapp_dev_manage iop_autocar oauth_tp_app smartapp_smart_game_openapi oauth_sessionkey smartapp_swanid_verify smartapp_opensource_openapi smartapp_opensource_recapi fake_face_detect_开放Scope vis-ocr_虚拟人物助理 idl-video_虚拟人物助理 smartapp_component smartapp_cserver_meta', 'session_secret': 'a9cef27de03291ec2ae0b872c11051b6'}'''
# encoding:utf-8

import base64
import requests


class AnimeDemo:
    def __init__(self, AK, SK):
        self.AK = AK
        self.SK = SK
        self.access_token = self.get_access_token()

    def get_access_token(self):
        token_host = 'https://aip.baidubce.com/oauth/2.0/token?grant_type=client_credentials&client_id={ak}&client_secret={sk}'.format(
            ak=self.AK, sk=self.SK)
        header = {'Content-Type': 'application/json; charset=UTF-8'}
        response = requests.post(url=token_host, headers=header)
        content = response.json()
        access_token = content.get("access_token")
        return access_token

    def baidu_selfie_anime(self, image_path, save_path):

        request_url = "https://aip.baidubce.com/rest/2.0/image-process/v1/selfie_anime"
        # 二进制方式打开图片文件
        f = open(image_path, 'rb')
        img = base64.b64encode(f.read())
        params = {"image": img, "option": "cartoon"}
        request_url = request_url + "?access_token=" + self.access_token
        headers = {'content-type': 'application/x-www-form-urlencoded'}
        try:
            response = requests.post(request_url, data=params, headers=headers)
            if response.status_code == 200:
                result = response.json()
                #print(result)
                image = result.get("image")
                if image:
                    img_data = base64.b64decode(image)
                    with open(save_path, "wb") as f:
                        f.write(img_data)
                    return {"msg": "完成"}
            return {"msg": "失败"}
        except Exception as e:
            return {"msg": "失败：%s" % e}


if __name__ == '__main__':
    AK = "mKBognBcqpp0NVHSpGDyUPma"  # 官网获取的AK 需要你先开通和创建应用
    SK = "edxmdTmlxB6egXrKrmpQGs3wihHNGoyX"  # 官网获取的SK
    anime_obj = AnimeDemo(AK=AK, SK=SK)
    res = anime_obj.baidu_selfie_anime("vscode/manhua/touxiang.jpg",
                                       "vscode/manhua/卡通.jpg")
    print("完成")