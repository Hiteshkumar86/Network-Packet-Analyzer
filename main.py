from scapy.all import sniff, IP, TCP, UDP, ICMP
from datetime import datetime
import csv

packet_count = 0


def analyze_packet(packet, csv_writer):
    global packet_count

    if IP in packet:
        packet_count += 1

        source_ip = packet[IP].src
        destination_ip = packet[IP].dst
        packet_size = len(packet)

        if TCP in packet:
            protocol = "TCP"
            source_port = packet[TCP].sport
            destination_port = packet[TCP].dport

        elif UDP in packet:
            protocol = "UDP"
            source_port = packet[UDP].sport
            destination_port = packet[UDP].dport

        elif ICMP in packet:
            protocol = "ICMP"
            source_port = "-"
            destination_port = "-"

        else:
            protocol = "Other"
            source_port = "-"
            destination_port = "-"

        timestamp = datetime.now().strftime(
            "%Y-%m-%d %H:%M:%S"
        )

        print("\n" + "=" * 50)
        print(f"Packet Number  : {packet_count}")
        print(f"Timestamp      : {timestamp}")
        print(f"Source IP      : {source_ip}")
        print(f"Destination IP : {destination_ip}")
        print(f"Protocol       : {protocol}")
        print(f"Packet Size    : {packet_size} bytes")
        print(f"Source Port    : {source_port}")
        print(f"Destination Port: {destination_port}")
        print("=" * 50)

        csv_writer.writerow([
            packet_count,
            timestamp,
            source_ip,
            destination_ip,
            protocol,
            packet_size,
            source_port,
            destination_port
        ])


def start_analyzer():
    print("\n====================================")
    print("      NETWORK PACKET ANALYZER")
    print("====================================")
    print("Capturing packet metadata...")
    print("Press CTRL + C to stop.\n")

    try:
        with open(
            "packet_log.csv",
            "w",
            newline="",
            encoding="utf-8"
        ) as file:

            writer = csv.writer(file)

            writer.writerow([
                "Packet Number",
                "Timestamp",
                "Source IP",
                "Destination IP",
                "Protocol",
                "Packet Size",
                "Source Port",
                "Destination Port"
            ])

            sniff(
                filter="ip",
                prn=lambda packet: analyze_packet(
                    packet, writer
                ),
                store=False
            )

    except KeyboardInterrupt:
        print("\nPacket capturing stopped.")

    except Exception as error:
        print(f"\nError: {error}")
        print("Try running VS Code as Administrator.")

    finally:
        print(f"\nTotal Packets Captured: {packet_count}")
        print("Network Analyzer Closed.")
        print("Packet log saved as packet_log.csv")


if __name__ == "__main__":
    start_analyzer()