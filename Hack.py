import uuid

def generate_link():
    # إنشاء رابط فريد مع معرف عشوائي
    uid = str(uuid.uuid4())[:8]
    
    # الموقع الفعلي الذي سيتم تحديده (استبدل هذا بعنوان الموقع الفعلي الذي ترغب في استخدامه)
    site_url = f"https://your-site.com/track?id={uid}"  # استخدم رابطك الفعلي هنا
    
    link = site_url
    return link

def display_rights():
    # عرض حقوقك كمطور
    print("\n[+] تم التطوير بواسطة 𝑫𝑨𝑹𝑲 𝑯𝑨𝑪𝑲𝑬𝑹")
    print("[+] رابط قناتي على Telegram: https://t.me/+PFbp1Ayc_1I3ZTFk")
    print("[+] يمكنكم استخدام هذه الأداة وفقًا للقوانين المعتمدة.")

def main():
    print("أداة توليد رابط تحديد الموقع\n")

    while True:
        # توليد رابط فريد مع الموقع
        link = generate_link()
        print(f"[+] رابط فريد تم إنشاؤه: {link}")
        
        # عرض الحقوق كمطور
        display_rights()
        
        # خيار لإعادة التوليد أو الخروج
        choice = input("\nهل ترغب في توليد رابط آخر؟ (نعم/لا): ").strip().lower()
        if choice != "نعم":
            break

if __name__ == "__main__":
    main()
