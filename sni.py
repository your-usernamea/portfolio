# كود Python لتوليد قائمة مضيفات SNI محتملة
# لا يحتاج إلى إنترنت، فقط ينشئ قائمة لاختبارها لاحقًا

# قائمة بالمواقع المحتملة (مواقع حكومية مغربية وخدمات شائعة)
hosts = [
    "www.iam.ma",
    "www.health.gov.ma",
    "www.education.gov.ma",
    "www.maroc.ma",
    "www.tgr.gov.ma",
    "www.covid19.gov.ma",
    "www.justice.gov.ma",
    "www.finances.gov.ma",
    "www.emploi.gov.ma",
    "web.whatsapp.com",
    "api.whatsapp.com",
    "m.facebook.com"
]

# قائمة بخوادم DNS من KOFnet
dns_servers = [
    "196.200.150.3",  # خادم المغرب للاتصالات (أكثر احتمالًا ليكون Zero-Rated)
    "172.217.18.14"   # خادم جوجل (أقل احتمالًا بناءً على نتيجة الـ ping)
]

# دالة لحفظ القائمة في ملف
def save_sni_list():
    with open("sni_list.txt", "w") as f:
        f.write("=== مضيفات SNI محتملة ===\n")
        f.write("المضيفات (للاستخدام في HttpCustom):\n")
        f.write("\n".join(hosts))
        f.write("\n\n=== خوادم DNS محتملة ===\n")
        f.write("\n".join(dns_servers))
    print("تم حفظ القائمة في sni_list.txt")

# تشغيل الدالة
if __name__ == "__main__":
    print("توليد قائمة مضيفات SNI...")
    save_sni_list()