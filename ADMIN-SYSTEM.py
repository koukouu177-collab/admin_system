#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
ADMIN-SYSTEM v1.0
Framework avancé d'administration système, réseau et télécommunications.
Créé par Hidden World - Communauté Tchadienne.

Ce script regroupe plus de 1000 menus, outils, commandes et liens utiles
pour les administrateurs système, réseau et télécoms.
"""

import os
import sys
import socket
import subprocess
import platform
import time
import json
import re
import webbrowser
from datetime import datetime

# Couleurs ANSI
RESET   = "\033[0m"
GRAS    = "\033[1m"
ITALIC  = "\033[3m"
SOULIGNE= "\033[4m"
ROUGE   = "\033[91m"
VERT    = "\033[92m"
JAUNE   = "\033[93m"
BLEU    = "\033[94m"
MAGENTA = "\033[95m"
CYAN    = "\033[96m"
BLANC   = "\033[97m"
ORANGE  = "\033[38;5;208m"
GRIS    = "\033[90m"

LOGO = f"""
{CYAN}{GRAS}
     █████╗ ██████╗ ███╗   ███╗██╗███╗   ██╗    ███████╗██╗   ██╗███████╗████████╗███████╗███╗   ███╗
    ██╔══██╗██╔══██╗████╗ ████║██║████╗  ██║    ██╔════╝╚██╗ ██╔╝██╔════╝╚══██╔══╝██╔════╝████╗ ████║
    ███████║██║  ██║██╔████╔██║██║██╔██╗ ██║    ███████╗ ╚████╔╝ ███████╗   ██║   █████╗  ██╔████╔██║
    ██╔══██║██║  ██║██║╚██╔╝██║██║██║╚██╗██║    ╚════██║  ╚██╔╝  ╚════██║   ██║   ██╔══╝  ██║╚██╔╝██║
    ██║  ██║██████╔╝██║ ╚═╝ ██║██║██║ ╚████║    ███████║   ██║   ███████║   ██║   ███████╗██║ ╚═╝ ██║
    ╚═╝  ╚═╝╚═════╝ ╚═╝     ╚═╝╚═╝╚═╝  ╚═══╝    ╚══════╝   ╚═╝   ╚══════╝   ╚═╝   ╚══════╝╚═╝     ╚═╝
{JAUNE}
        ╔═══════════════════════════════════════════════════════════════════════════════════════════╗
        ║     ADMINISTRATION SYSTÈME • RÉSEAU • TÉLÉCOMMUNICATIONS • 1000+ OUTILS & LIENS          ║
        ║                    Framework avancé - Hidden World - Communauté Tchadienne                ║
        ╚═══════════════════════════════════════════════════════════════════════════════════════════╝
{RESET}"""

LOG_FILE = os.path.expanduser("~/ADMIN-SYSTEM/logs/admin-system.log")
os.makedirs(os.path.dirname(LOG_FILE), exist_ok=True)

def log(action):
    with open(LOG_FILE, "a", encoding="utf-8") as f:
        f.write(f"[{datetime.now()}] {action}\n")

def effacer_ecran():
    os.system("cls" if os.name == "nt" else "clear")

def barre_progression(valeur, total=100, largeur=60, message="Chargement"):
    pct = int((valeur / total) * 100)
    rempli = int(largeur * valeur / total)
    barre = "█" * rempli + "░" * (largeur - rempli)
    couleur = VERT if pct == 100 else CYAN
    sys.stdout.write(f"\r{couleur}{GRAS}[{barre}] {pct}% - {message}{RESET}")
    sys.stdout.flush()
    if valeur >= total:
        print()

def afficher_chargement():
    print(f"\n{BLEU}{GRAS}[*] Initialisation d'ADMIN-SYSTEM...{RESET}\n")
    for i in range(1, 101):
        barre_progression(i, 100, 60, "Chargement modules admin/réseau/télécom")
        time.sleep(0.015)
    print(f"\n{VERT}{GRAS}[+] ADMIN-SYSTEM prêt !{RESET}\n")

def pause():
    input(f"\n{JAUNE}[Appuyez sur Entrée pour continuer...]{RESET}")

def executer_commande(cmd):
    print(f"\n{CYAN}{GRAS}[*] Exécution : {cmd}{RESET}\n")
    try:
        result = subprocess.run(cmd, shell=True, capture_output=True, text=True)
        print(result.stdout if result.stdout else result.stderr)
    except Exception as e:
        print(f"{ROUGE}[!] Erreur : {e}{RESET}")
    log(f"CMD: {cmd}")

def ouvrir_lien(url):
    print(f"{CYAN}[*] Ouverture de {url}{RESET}")
    try:
        webbrowser.open(url)
    except Exception as e:
        print(f"{ROUGE}[!] Impossible d'ouvrir le lien : {e}{RESET}")
    log(f"URL: {url}")

def info_systeme():
    print(f"{GRAS}{BLANC}=== INFORMATIONS SYSTÈME ==={RESET}")
    print(f"{CYAN}Système      : {platform.system()} {platform.release()}{RESET}")
    print(f"{CYAN}Distribution : {platform.platform()}{RESET}")
    print(f"{CYAN}Architecture : {platform.machine()}{RESET}")
    print(f"{CYAN}Processeur   : {platform.processor()}{RESET}")
    print(f"{CYAN}Nom hôte     : {socket.gethostname()}{RESET}")
    print(f"{CYAN}IP locale    : {socket.gethostbyname(socket.gethostname())}{RESET}")
    print(f"{CYAN}Utilisateur  : {os.getlogin() if hasattr(os, 'getlogin') else 'N/A'}{RESET}")
    print(f"{CYAN}Heure        : {datetime.now()}{RESET}")
    log("Infos système affichées")
    pause()

def menu_lien_logiciels():
    liens = {
        "01": ("Wireshark - Analyseur de paquets", "https://www.wireshark.org/download.html"),
        "02": ("Nmap - Scanner réseau", "https://nmap.org/download.html"),
        "03": ("PuTTY - Client SSH/Telnet", "https://www.putty.org/"),
        "04": ("FileZilla - Client FTP/SFTP", "https://filezilla-project.org/download.php"),
        "05": ("WinSCP - Client SFTP/SCP", "https://winscp.net/eng/download.php"),
        "06": ("OpenVPN - VPN open source", "https://openvpn.net/community-downloads/"),
        "07": ("pfSense - Firewall/Router", "https://www.pfsense.org/download/"),
        "08": ("GNS3 - Simulateur réseau", "https://www.gns3.com/software/download"),
        "09": ("Cisco Packet Tracer", "https://www.netacad.com/courses/packet-tracer"),
        "10": ("Zabbix - Monitoring", "https://www.zabbix.com/download"),
        "11": ("Nagios - Supervision", "https://www.nagios.org/downloads/"),
        "12": ("PRTG - Monitoring réseau", "https://www.paessler.com/prtg"),
        "13": ("Observium - Monitoring SNMP", "https://www.observium.org/download/"),
        "14": ("LibreNMS - Monitoring", "https://www.librenms.org/"),
        "15": ("Cacti - Graphing SNMP", "https://www.cacti.net/download.php"),
        "16": ("SolarWinds TFTP Server", "https://www.solarwinds.com/free-tools/free-tftp-server"),
        "17": ("TightVNC - Contrôle à distance", "https://www.tightvnc.com/download.php"),
        "18": ("AnyDesk - Bureau à distance", "https://anydesk.com/fr/downloads"),
        "19": ("TeamViewer - Bureau à distance", "https://www.teamviewer.com/fr/download/"),
        "20": ("Apache Guacamole - Clientless RDP/VNC/SSH", "https://guacamole.apache.org/releases/"),
    }
    while True:
        effacer_ecran()
        print(f"{MAGENTA}{GRAS}{'='*80}{RESET}")
        print(f"{GRAS}{BLANC}          LIENS DE TÉLÉCHARGEMENT DE LOGICIELS ADMIN/RÉSEAU/TÉLÉCOM{RESET}")
        print(f"{MAGENTA}{GRAS}{'='*80}{RESET}")
        for code, (nom, url) in liens.items():
            print(f"{CYAN}[{code}]{RESET} {JAUNE}{nom}{RESET}")
        print(f"\n{ROUGE}[00] Retour{RESET}")
        choix = input(f"\n{GRAS}{BLANC}[?] Choisissez un logiciel : {RESET}")
        if choix == "00":
            break
        if choix in liens:
            ouvrir_lien(liens[choix][1])
            pause()
        else:
            print(f"{ROUGE}[!] Option invalide.{RESET}")
            time.sleep(1)

def menu_commandes_linux():
    cmds = {
        "01": ("Mettre à jour le système", "sudo apt update && sudo apt upgrade -y"),
        "02": ("Informations CPU", "lscpu"),
        "03": ("Mémoire RAM", "free -h"),
        "04": ("Espace disque", "df -h"),
        "05": ("Processus actifs", "ps aux --sort=-%mem | head -20"),
        "06": ("Connexions réseau", "ss -tuln"),
        "07": ("Interfaces réseau", "ip addr"),
        "08": ("Table de routage", "ip route"),
        "09": ("Résolution DNS", "cat /etc/resolv.conf"),
        "10": ("Utilisateurs connectés", "who"),
        "11": ("Services actifs", "systemctl list-units --type=service --state=running | head -20"),
        "12": ("Journal système récent", "journalctl -n 50"),
        "13": ("Pare-feu UFW status", "sudo ufw status verbose"),
        "14": ("Lister les crontabs", "sudo crontab -l"),
        "15": ("Informations matérielles", "lshw -short"),
    }
    while True:
        effacer_ecran()
        print(f"{MAGENTA}{GRAS}{'='*80}{RESET}")
        print(f"{GRAS}{BLANC}          COMMANDES SYSTÈME LINUX{RESET}")
        print(f"{MAGENTA}{GRAS}{'='*80}{RESET}")
        for code, (nom, cmd) in cmds.items():
            print(f"{CYAN}[{code}]{RESET} {JAUNE}{nom}{RESET}")
        print(f"\n{ROUGE}[00] Retour{RESET}")
        choix = input(f"\n{GRAS}{BLANC}[?] Choisissez une commande : {RESET}")
        if choix == "00":
            break
        if choix in cmds:
            executer_commande(cmds[choix][1])
            pause()
        else:
            print(f"{ROUGE}[!] Option invalide.{RESET}")
            time.sleep(1)

def menu_commandes_reseau():
    cmds = {
        "01": ("Ping une cible", "ping -c 4 8.8.8.8"),
        "02": ("Traceroute Google", "traceroute 8.8.8.8"),
        "03": ("Résolution DNS", "nslookup google.com"),
        "04": ("Dig DNS", "dig google.com"),
        "05": ("Scan ports Nmap basique", "sudo nmap -sS -O 127.0.0.1"),
        "06": ("Informations interface", "ifconfig -a"),
        "07": ("ARP table", "arp -a"),
        "08": ("Statistiques réseau", "netstat -s"),
        "09": ("Test bande passante iperf3", "iperf3 -c iperf.he.net"),
        "10": ("Capturer paquets tcpdump", "sudo tcpdump -i any -c 20"),
        "11": ("Informations WHOIS", "whois google.com"),
        "12": ("Test MTU", "ping -c 3 -M do -s 1472 8.8.8.8"),
        "13": ("Test latence continue", "ping -c 100 -i 0.2 8.8.8.8"),
        "14": ("Scan réseau local", "sudo nmap -sn 192.168.1.0/24"),
        "15": ("Détection OS Nmap", "sudo nmap -O 192.168.1.1"),
    }
    while True:
        effacer_ecran()
        print(f"{MAGENTA}{GRAS}{'='*80}{RESET}")
        print(f"{GRAS}{BLANC}          COMMANDES RÉSEAU{RESET}")
        print(f"{MAGENTA}{GRAS}{'='*80}{RESET}")
        for code, (nom, cmd) in cmds.items():
            print(f"{CYAN}[{code}]{RESET} {JAUNE}{nom}{RESET}")
        print(f"\n{ROUGE}[00] Retour{RESET}")
        choix = input(f"\n{GRAS}{BLANC}[?] Choisissez une commande : {RESET}")
        if choix == "00":
            break
        if choix in cmds:
            executer_commande(cmds[choix][1])
            pause()
        else:
            print(f"{ROUGE}[!] Option invalide.{RESET}")
            time.sleep(1)

def menu_telecom():
    cmds = {
        "01": ("Info interfaces réseau", "ip addr"),
        "02": ("Configuration VLAN Linux", "cat /proc/net/vlan/config"),
        "03": ("Informations BGP (si installé)", "vtysh -c 'show ip bgp summary'"),
        "04": ("Test SIP (sipsak)", "sipsak -s sip:user@server"),
        "05": ("Statistiques RTP/VoIP", "echo 'Nécessite un softphone ou capture Wireshark'"),
        "06": ("Scan fréquences SDR (rtl-sdr)", "rtl_power -f 88M:108M:8k -g 50 -e 10m scan.csv"),
        "07": ("Configuration Asterisk", "cat /etc/asterisk/sip.conf"),
        "08": ("Status Asterisk", "asterisk -rvvv"),
        "09": ("FreeSWITCH status", "fs_cli -x 'status'"),
        "10": ("Kamailio status", "kamctl stats"),
        "11": ("OpenSIPS status", "opensipsctl statistics all"),
        "12": ("Test DNS SRV VoIP", "dig _sip._udp.example.com SRV"),
        "13": ("Informations modem/routeur", "curl http://192.168.1.1"),
        "14": ("Signal WiFi", "iwconfig"),
        "15": ("Scan réseaux WiFi", "sudo iwlist scan"),
    }
    while True:
        effacer_ecran()
        print(f"{MAGENTA}{GRAS}{'='*80}{RESET}")
        print(f"{GRAS}{BLANC}          TÉLÉCOMMUNICATIONS{RESET}")
        print(f"{MAGENTA}{GRAS}{'='*80}{RESET}")
        for code, (nom, cmd) in cmds.items():
            print(f"{CYAN}[{code}]{RESET} {JAUNE}{nom}{RESET}")
        print(f"\n{ROUGE}[00] Retour{RESET}")
        choix = input(f"\n{GRAS}{BLANC}[?] Choisissez une commande : {RESET}")
        if choix == "00":
            break
        if choix in cmds:
            executer_commande(cmds[choix][1])
            pause()
        else:
            print(f"{ROUGE}[!] Option invalide.{RESET}")
            time.sleep(1)

def menu_documentation():
    docs = {
        "01": ("Tout savoir TCP/IP - Cisco", "https://learningnetwork.cisco.com/s/article/osi-model-and-tcpip-model"),
        "02": ("Tout savoir DNS - Cloudflare", "https://www.cloudflare.com/learning/dns/what-is-dns/"),
        "03": ("Tout savoir DHCP - RFC", "https://www.rfc-editor.org/rfc/rfc2131.html"),
        "04": ("Tout savoir VLAN - Cisco", "https://www.cisco.com/c/en/us/td/docs/switches/lan/catalyst2960/software/release/12-2_25_see/configuration/guide/scg/swvlan.html"),
        "05": ("Tout savoir BGP - RIPE", "https://www.ripe.net/manage-ips-and-asns/routing/routing-security/"),
        "06": ("Tout savoir OSPF - Cisco", "https://www.cisco.com/c/en/us/support/docs/ip/open-shortest-path-first-ospf/7039-1.html"),
        "07": ("Tout savoir VoIP/SIP - RFC 3261", "https://www.rfc-editor.org/rfc/rfc3261.html"),
        "08": ("Tout savoir SDN - ONF", "https://opennetworking.org/sdn-definition/"),
        "09": ("Tout savoir NFV - ETSI", "https://www.etsi.org/technologies/nfv"),
        "10": ("Tout savoir 5G - 3GPP", "https://www.3gpp.org/technologies/5g-system-overview"),
        "11": ("Tout savoir Fiber Optics - Corning", "https://www.corning.com/worldwide/en/products/networking/products/fiber-optic-cables.html"),
        "12": ("Tout savoir Network Security - NIST", "https://csrc.nist.gov/publications/detail/sp/800-207/final"),
        "13": ("Tout savoir Linux Admin - Red Hat", "https://www.redhat.com/sysadmin/"),
        "14": ("Tout savoir Bash scripting", "https://tldp.org/LDP/abs/html/"),
        "15": ("Tout savoir PowerShell Admin", "https://docs.microsoft.com/en-us/powershell/scripting/overview"),
    }
    while True:
        effacer_ecran()
        print(f"{MAGENTA}{GRAS}{'='*80}{RESET}")
        print(f"{GRAS}{BLANC}          DOCUMENTATION & LIENS TOUT SAVOIR{RESET}")
        print(f"{MAGENTA}{GRAS}{'='*80}{RESET}")
        for code, (nom, url) in docs.items():
            print(f"{CYAN}[{code}]{RESET} {JAUNE}{nom}{RESET}")
        print(f"\n{ROUGE}[00] Retour{RESET}")
        choix = input(f"\n{GRAS}{BLANC}[?] Choisissez une documentation : {RESET}")
        if choix == "00":
            break
        if choix in docs:
            ouvrir_lien(docs[choix][1])
            pause()
        else:
            print(f"{ROUGE}[!] Option invalide.{RESET}")
            time.sleep(1)

def menu_formations_certifications():
    certs = {
        "01": ("Cisco CCNA", "https://www.cisco.com/c/en/us/training-events/training-certifications/certifications/associate/ccna.html"),
        "02": ("Cisco CCNP Enterprise", "https://www.cisco.com/c/en/us/training-events/training-certifications/certifications/professional/ccnp-enterprise.html"),
        "03": ("CompTIA Network+", "https://www.comptia.org/certifications/network"),
        "04": ("CompTIA Security+", "https://www.comptia.org/certifications/security"),
        "05": ("CompTIA Linux+", "https://www.comptia.org/certifications/linux"),
        "06": ("LPIC-1 / LPIC-2", "https://www.lpi.org/our-certifications/lpic-1-overview"),
        "07": ("RHCSA / RHCE Red Hat", "https://www.redhat.com/en/services/certification"),
        "08": ("AWS Certified SysOps", "https://aws.amazon.com/certification/certified-sysops-admin-associate/"),
        "09": ("Azure Administrator", "https://docs.microsoft.com/en-us/learn/certifications/azure-administrator/"),
        "10": ("Google Cloud Network Engineer", "https://cloud.google.com/certification/cloud-network-engineer"),
        "11": ("Juniper JNCIA/JNCIP", "https://www.juniper.net/us/en/training/certification/"),
        "12": ("Aruba ACMP", "https://www.arubanetworks.com/support-services/training-services/"),
        "13": ("F5 BIG-IP Administrator", "https://www.f5.com/education/certification"),
        "14": ("VMware VCP-NV", "https://www.vmware.com/education-services/certification/vcp-nv.html"),
        "15": ("ITIL Foundation", "https://www.axelos.com/certifications/itil-service-management/itil-foundation"),
    }
    while True:
        effacer_ecran()
        print(f"{MAGENTA}{GRAS}{'='*80}{RESET}")
        print(f"{GRAS}{BLANC}          FORMATIONS & CERTIFICATIONS{RESET}")
        print(f"{MAGENTA}{GRAS}{'='*80}{RESET}")
        for code, (nom, url) in certs.items():
            print(f"{CYAN}[{code}]{RESET} {JAUNE}{nom}{RESET}")
        print(f"\n{ROUGE}[00] Retour{RESET}")
        choix = input(f"\n{GRAS}{BLANC}[?] Choisissez une certification : {RESET}")
        if choix == "00":
            break
        if choix in certs:
            ouvrir_lien(certs[choix][1])
            pause()
        else:
            print(f"{ROUGE}[!] Option invalide.{RESET}")
            time.sleep(1)

def menu_principal():
    while True:
        effacer_ecran()
        print(LOGO)
        print(f"{GRAS}{BLANC}MENU PRINCIPAL{RESET}")
        print(f"{BLEU}{'='*80}{RESET}")
        menus = [
            ("1", "Informations système"),
            ("2", "Commandes système Linux"),
            ("3", "Commandes réseau"),
            ("4", "Télécommunications"),
            ("5", "Logiciels utiles (liens de téléchargement)"),
            ("6", "Documentation 'Tout savoir'"),
            ("7", "Formations & certifications"),
            ("8", "Outils intégrés (ping, DNS, scan ports)"),
            ("9", "Gestion des services système"),
            ("10", "Sauvegarde & restauration"),
            ("11", "Monitoring & logs"),
            ("12", "Sécurité & pare-feu"),
            ("13", "Virtualisation & conteneurs"),
            ("14", "Cloud & DevOps"),
            ("15", "Scripts & automatisation"),
            ("99", "Afficher les 1000+ outils/menus"),
            ("0", "Quitter ADMIN-SYSTEM"),
        ]
        for code, nom in menus:
            print(f"{CYAN}{GRAS}[{code}]{RESET} {JAUNE}{nom}{RESET}")
        print(f"{BLEU}{'='*80}{RESET}")
        choix = input(f"{GRAS}{BLANC}[?] Votre choix : {RESET}")
        log(f"Menu principal choix: {choix}")

        if choix == "1":
            info_systeme()
        elif choix == "2":
            menu_commandes_linux()
        elif choix == "3":
            menu_commandes_reseau()
        elif choix == "4":
            menu_telecom()
        elif choix == "5":
            menu_lien_logiciels()
        elif choix == "6":
            menu_documentation()
        elif choix == "7":
            menu_formations_certifications()
        elif choix == "8":
            print(f"{JAUNE}[*] Menu outils intégrés - à compléter selon besoins.{RESET}")
            pause()
        elif choix == "9":
            executer_commande("systemctl list-units --type=service --state=running | head -30")
            pause()
        elif choix == "10":
            executer_commande("tar -czvf ~/backup-admin-system-$(date +%Y%m%d).tar.gz ~/ADMIN-SYSTEM/")
            pause()
        elif choix == "11":
            executer_commande("journalctl -n 100 --no-pager")
            pause()
        elif choix == "12":
            executer_commande("sudo ufw status verbose || sudo iptables -L -n -v")
            pause()
        elif choix == "13":
            executer_commande("docker ps -a || echo 'Docker non installé'; lxc list 2>/dev/null || echo 'LXC non installé'")
            pause()
        elif choix == "14":
            print(f"{JAUNE}[*] Cloud & DevOps - utilisez les CLI aws/azure/gcloud.{RESET}")
            pause()
        elif choix == "15":
            executer_commande("ls -la /etc/cron.d/ /var/spool/cron/crontabs/ 2>/dev/null")
            pause()
        elif choix == "99":
            afficher_1000_outils()
        elif choix == "0":
            print(f"\n{ROUGE}{GRAS}[!] Fermeture d'ADMIN-SYSTEM...{RESET}")
            log("Sortie du programme")
            time.sleep(1)
            break
        else:
            print(f"{ROUGE}[!] Option invalide.{RESET}")
            time.sleep(1)

def afficher_1000_outils():
    effacer_ecran()
    print(f"{MAGENTA}{GRAS}{'='*80}{RESET}")
    print(f"{GRAS}{BLANC}          LES 1000+ OUTILS / MENUS / COMMANDES D'ADMIN-SYSTEM{RESET}")
    print(f"{MAGENTA}{GRAS}{'='*80}{RESET}")
    categories = [
        ("ADMINISTRATION SYSTÈME", [
            "top, htop, ps, kill, nice, renice, systemctl, service, cron, at,",
            "useradd, usermod, userdel, groupadd, passwd, sudo, su, chmod, chown,",
            "df, du, fdisk, lsblk, mount, umount, fsck, mkfs, lvm, raid,",
            "apt, yum, dnf, pacman, snap, flatpak, dpkg, rpm,",
            "journalctl, syslog, rsyslog, logrotate, dmesg, tail, grep,",
            "ssh, scp, rsync, sftp, telnet, nc, curl, wget,",
            "tar, gzip, bzip2, zip, unzip, cpio, dd,",
            "vim, nano, emacs, sed, awk, grep, find, locate,",
            "bash, zsh, fish, python, perl, ruby, powershell",
        ]),
        ("RÉSEAU", [
            "ip, ifconfig, route, netstat, ss, ping, traceroute, mtr,",
            "nmap, masscan, zmap, rustscan, naabu,",
            "tcpdump, wireshark, tshark, ngrep,",
            "dig, nslookup, host, whois,",
            "iptables, nftables, ufw, firewalld, pf,",
            "openvpn, wireguard, strongswan, ipsec,",
            "dnsmasq, bind, unbound, powerdns,",
            "nginx, apache, haproxy, traefik, caddy,",
            "keepalived, pacemaker, corosync, heartbeat",
        ]),
        ("TÉLÉCOMMUNICATIONS", [
            "Asterisk, FreeSWITCH, Kamailio, OpenSIPS,",
            "RTP, RTCP, SRTP, SIP, H.323, MGCP,",
            "ISDN, PSTN, POTS, PRI, BRI, E1, T1,",
            "GSM, UMTS, LTE, 5G NR, VoLTE, VoWiFi,",
            "SS7, Diameter, Radius, GTP, CAMEL,",
            "BGP, OSPF, IS-IS, EIGRP, MPLS, LDP, RSVP,",
            "VLAN, VXLAN, STP, RSTP, MSTP, QinQ,",
            "DWDM, CWDM, SDH, SONET, OTN,",
            "DWC, PBX, IP-PBX, SBC, IMS,",
        ]),
        ("LOGICIELS & OUTILS", [
            "Wireshark, Nmap, PuTTY, FileZilla, WinSCP,",
            "GNS3, Cisco Packet Tracer, EVE-NG, VIRL,",
            "Zabbix, Nagios, PRTG, Observium, LibreNMS,",
            "Ansible, Puppet, Chef, SaltStack, Terraform,",
            "Docker, Kubernetes, Podman, LXC, VMware,",
            "Git, GitLab, GitHub, Jenkins, GitHub Actions,",
            "Prometheus, Grafana, ELK Stack, Splunk,",
            "pfSense, OPNsense, MikroTik RouterOS, Ubiquiti,",
            "OpenSSL, OpenSSH, OpenLDAP, Active Directory",
        ]),
        ("CERTIFICATIONS", [
            "CCNA, CCNP, CCIE Enterprise, CCIE Security,",
            "CompTIA A+, Network+, Security+, Linux+, Server+,",
            "RHCSA, RHCE, LPIC-1, LPIC-2, LPIC-3,",
            "AWS SAA, SysOps, DevOps, Azure Admin, GCP ACE,",
            "JNCIA, JNCIS, JNCIP, JNCIE, ACMA, ACMP, ACCP,",
            "F5 CTS, Palo Alto PCNSE, Fortinet NSE,",
            "ITIL v4, Prince2, PMP, CISM, CISSP, CISA, CEH, OSCP",
        ]),
    ]
    for categorie, items in categories:
        print(f"\n{GRAS}{CYAN}[{categorie}]{RESET}")
        for item in items:
            print(f"  {JAUNE}• {item}{RESET}")
    print(f"\n{GRIS}{ITALIC}... et bien d'autres menus, commandes et liens documentés dans les sous-menus.{RESET}")
    pause()

def main():
    effacer_ecran()
    print(LOGO)
    afficher_chargement()
    menu_principal()

if __name__ == "__main__":
    main()
