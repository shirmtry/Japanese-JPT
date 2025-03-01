import tkinter as tk
from tkinter import messagebox, simpledialog
import random

# Các bộ từ vựng
vocab_sets = {
    "B1": {
        "watashi": "tôi", "namae": "tên", "kuni": "nước", "nihon": "nhật", "amerika": "mỹ", "itaria": "ý",
        "osutoraria": "úc", "konkoku": "hàn quốc", "tai": "thái lan", "roshia": "nga", "koukou": "thpt", "daigaku": "đại học",
        "nihongogatsukou": "Trường học tiếng nhật", "shigoto": "công việc", "gakusei": "học sinh", "sensei": "giáo viên", "kyoushi": "giáo viên",
        "kaishain": "nhân viên công ty", "shain": "nhân viên công ty", "chin": "Anh/chị", "zin": "người", "dochira": "nào",
        "wakunihadochiradesu": "Bạn là người nước nào ?", "hazimemoshite": "Câu chào khi lần đầu gặp mặt", "yotoshikuonegaishimasu": "Rất mong được sự giúp đỡ của anh/chị",
        "kochirakoso": "chính tôi cũng thế", "anoe": "À", "sumimasen": "xin lỗi", "soudesuka": "thế à", "hai": "vâng", "iie": "không",
        "tanjouki": "sinh nhật", "gatsu": "tháng", "baraziku": "brazil", "chii": "tuổi", "nichi": "ngày", "itsu": "bao giờ",
        "shumi": "sở thích", "supotsu": "thể thao", "satsuka": "bóng đá", "tenisu": "quần vợt", "suiei": "bơi", "eiga": "điện ảnh",
        "ongaka": "âm nhạc", "dokusho": "đọc sách", "ryouri": "nấu ăn", "ryokou": "du lịch", "nan": "gì", "a": "a", "waa": "ôi",
        "onezidesune": "giống nhau nhỉ"
    },
    "B2": {
        "kokokochira": "chỗ này", "sokosochira": "chỗ đấy", "asokoachira": "chỗ kia", "infomeshon": "thông tin", "ATM": "Máy tiền",
        "esukaruta": "cầu thang cuốn", "erubeta": "thang máy", "kitsuenzo": "chỗ hút thuốc", "toiru": "toa lét", "ruzi": "chỗ tính tiền",
        "kitsuchiten": "siêu thị", "100enshotsupu": "cửa hàng 100 yên", "rusutoran": "nhà hàng", "chika": "dưới lòng đất", "kamera": "máy ảnh",
        "keitaidenwa": "điện thoại cầm tay", "pasokon": "máy vi tính", "denshizisho": "từ điển điện tử", "kutsu": "Giầy", "keshigoma": "tẩy",
        "pen": "bút", "toirutsutopepu": "giấy toa lét", "hon": "sách", "abura": "dầu", "keki": "bánh ngọt", "kome": "gạo", "tamago": "trứng",
        "pan": "bánh mì", "mizu": "nước", "tenin": "người bán hàng", "kai": "tầng", "ya": "cửa hàng", "doko": "đâu", 
        "ichitsushiyaimase": "xin chào quý khách", "arigatoigodiimasu": "cảm ơn", "kore": "cái này", "sore": "cái đấy", "are": "cái kia", 
        "kono": "này", "sono": "đấy", "ano": "kia", "kaban": "túi", "zubon": "quần", "shiyatsu": "áo phông", "tokei": "đồng hồ", 
        "en": "yên", "ikuchi": "bao nhiêu", "ziya": "thế thì", "chikana": "cá", "niku": "thịt", "guuniku": "thịt bò", "toriniku": "thịt gà",
        "butaniku": "thịt lợn", "ringo": "táo", "ichigo": "dâu tây", "yachii": "rau", "ryouri": "món ăn", "korehachikananoryouri": "đây là món cá",
        "kari": "cơ ri", "supu": "súp", "tonkatsu": "món thịt lợn chiên", "hanbagu": "món thịt băm rán", "gohan": "cơm",
        "gohanwo2tsukudachii": "cho tôi 2 bát cơm", "raisu": "gạo", "jasu": "nước hoa quả", "kohi": "cà phê", "koucha": "trà đen", "cha": "trà",
        "biru": "bia", "rain": "rượu vang", "indo": "ấn độ", "doitsu": "đức", "furansu": "pháp", "saifu": "ví", "eigo": "tiếng anh",
        "go": "tiến", "tsu": "cái", "gore": "ai", "chuumonwonegaishimasu": "cho tôi gọi món", "douzo": "xin mời", "kochirahedouzo": "xin mời đến đây",
        "menya": "thực đơn", "shoushouomachikudasa": "xin đợi 1 chút"
    },
    "B3": {
        "shiumatsu": "cuối tuần", "ima": "bây giờ", "gozen": "buổi sáng", "hiru": "buổi trưa", "ginkou": "ngân hàng", "taiikukan": "nhà chơi thể thao",
        "toshokan": "thư viện", "byouin": "bệnh viện", "yuubinkyoku": "bưu điện", "jugyou": "giờ học", "tesuto": "bài kiểm tra",
        "yasu": "giờ nghỉ", "zikan": "thời gian", "zi": "giờ", "fun": "phút", "ima, 9 zi 20 fundesu": "bây giờ là 9 giờ 20 phút",
        "youbi": "thứ", "sukezyuru": "lịch làm việc", "arubaito": "việc làm thêm", "suki": "trượt tuyết", "patei": "bữa tiệc",
        "zihan": "giờ rưỡi", "babekyu": "bữa tiệc thịt nướng", "hanabi": "pháo hoa", "hanami": "ngắm hoa", "homusutei": "trọ người bản xứ",
        "matsu": "lễ hội", "umi": "biển", "kouen": "công viên", "sakura": "hoa anh đào", "sake": "rượu", "sushi": "món sushi",
        "basu": "xe buýt", "bentou": "cơm hộp", "ryuugakusei": "lưu học sinh", "1 nen": "năm thứ nhất", "haru": "mùa xuân",
        "natsu": "mùa hè", "aki": "mùa thu", "fuyu": "mùa đông", "gorudenuaku": "tuần lễ vàng", "nani": "gì",
        "ikimasu": "đi", "kaerimasu": "về", "nomimasu": "uống", "tabemasu": "ăn", "mimasu": "xem", "shimasu": "làm",
        "sukimashimasu": "trượt tuyết", "iidesune": "thích nhỉ", "etsu": "sao", "hee": "à thế à", "asa": "buổi sáng",
        "foru": "buổi đêm", "mainichi": "hàng ngày", "maiasa": "hàng sáng", "maiban": "hàng tối", "asagohan": "cơm sáng",
        "hirugohan": "cơm trưa", "uchi": "nhà", "kaishu": "công ty", "gatsukou": "trường học", "konbini": "cửa hàng tiện lợi",
        "gyuuniyuu": "sữa bò", "kudamono": "hoa quả", "sarada": "món sa lát"
    },
    "B4": {
        "gyuuniyuu": "sữa bò", "kudamono": "hoa quả", "sarada": "món sa lát",
        "chika": "gần", "1nichi": "một ngày", "mata": "lại", "chou": "hôm nay", "ashita": "ngày mai", "asatsute": "ngày kia",
        "kinou": "hôm qua", "ototoi": "hôm kia", "senshuu": "tuần trước", "shuumatsu": "cuối tuần", "ie": "nhà", "heya": "phòng",
        "depato": "bách hóa", "bijutsukan": "bảo tàng mỹ thuật", "gemu": "trò chơi", "kazoku": "gia đình", "koibito": "người yêu",
        "tomodachi": "bạn", "rumumeito": "bạn cùng phòng", "dokoka": "đâu", "aimasu": "gặp", "tsukirima": "làm", "kaimono shimasu": "mua hàng",
        "shokuzi shimasu": "ăn", "sentaku shimasu": "giặt", "sorekara": "dọn vệ sinh", "1hitoride": "sau đó", "kesa": "sáng nay",
        "kirai": "ghét", "senyetsu": "tháng trước", "kyonen": "năm ngoái", "kaze": "bệnh cúm", "tenki": "thời tiết", "bangohan": "cơm tối",
        "fuku": "quần áo", "noborimasu": "leo", "hairimasu": "vào", "isoga": "vào suối nước nóng", "omoshiroi": "vui",
        "kimochigaii": "dễ chịu", "taka": "đắt", "patsukonhatakakatsutadesu": "máy vi tính đắt", "yasu": "rẻ", "tanoshii": "vui",
        "muzuka": "khó", "katan": "đơn giản", "taihen": "vất vả", "hima": "nhàn rỗi", "doushite": "tại sao", "kondo": "lần tới",
        "konban": "tối nay", "kotoshi": "năm nay", "chiinen": "sang năm", "snime": "phim hoạt hình", "e": "bức tranh", "keshiki": "phong cảnh",
        "zitensha": "xe đạp", "shashin": "bức ảnh", "torimasu": "chụp", "karimasu": "mượn", "hoshii": "muốn", "suki": "thích",
        "ryou": "ký túc xá", "iroiro": "nhiều", "sorehayokatsudesune": "thế thì tốt nhỉ", "tsusu": "nước sốt", "piza": "bánh pizza",
        "minasan": "quý vị", "konshuu": "tuần này", "riishuu": "tuần sau", "kongetsu": "tháng này", "riigetsu": "tháng sau",
        "karaoke": "karaoke", "konsato": "buổi hòa nhạc", "shiai": "trận đấu", "seru": "bán hạ giá", "chiketsuto": "vé",
        "chizu": "bản đồ", "doraibu": "lái ô tô đi chơi", "mizugi": "quần áo tắm", "yakyuu": "bóng chuyền", "yakusoku": "hẹn",
        "youzi": "công chuyện", "mai": "cái", "arimasu": "có", "zannen": "tiếc", "itsusho": "cùng", "aa": "ôi",
        "aa,nichiyoubi": "ôi chủ nhật thì", "tsuto": "không được rồi", "sumimasen": "xin lỗi", "matakondo": "hẹn lần tới",
        "waa": "ôi", "sukiyaki": "một món lẩu", "asobimasu": "chơi", "zebi": "nhất định", "mada": "chưa", "mou": "rồi",
        "soushimashou": "chúng ta làm thế nhé", "wakarimashita": "hiểu rồi"
    },
    "B5": {
        "ryoushin": "Bố mẹ", "chichi": "Bố", "haha": "Mẹ", "kyoudai": "Anh em", "ani": "Anh trai", "ane": "Chị gái", "otouto": "Em trai", "imouto": "Em gái",
        "otsuto": "Chồng", "tsuma": "Vợ", "kodomo": "Con", "musuko": "Con trai", "musume": "Con gái", "otouchin": "Bố", "sumimasu": "Sống", "imasu": "Có",
        "watashihaatoutogaimasu": "Tôi có em trai", "goshuzin": "Chồng", "akusan": "Vợ", "senpai": "Đàn anh", "kouhai": "Đàn em", "usagi": "Thỏ", "karada": "Cơ thể",
        "ashi": "Chân", "kao": "Mặt", "kami": "Tóc", "kuchi": "Mồm", "hana": "Mũi", "me": "Mắt", "mimi": "Tai", "atamagaii": "Thông minh", "katsukoii": "Đẹp trai",
        "kawaii": "Xinh", "segatakai": "Người cao", "nagai": "Dài", "mizikai": "Ngắn", "yasashi": "Hiền", "kuroi": "Đen", "shiroi": "Trắng", "chairoi": "Nâu",
        "banki": "Khỏe", "shinsetsu": "Thân thiện", "mazime": "Nghiêm túc", "jouzu": "Giỏi", "heta": "Kém"
    },
    "B7": {
        "atama": "đầu", "kaiwa": "hội thoại", "sakubun": "bài văn", "kurasumeito": "bạn học", "zatsushi": "tạp chí", "jogingu": "chạy bộ", "seikastu": "cuộc sống",
        "tenchou": "cửa hàng trưởng", "nitsuki": "nhật ký", "hazi": "đầu tiên", "hitorigurashi": "sống một mình", "hiragana": "chữ hiragana", "heizitsu": "ngày thường",
        "maishu": "hàng tuần", "senshu": "tuyển thủ", "sofu": "ông", "haziamesu": "bắt đầu", "wakaremasu": "chia tay", "dandan": "dần dần", "haziate": "lúc đầu",
        "sorede": "do đó", "eakon": "điều hòa nhiệt độ", "nyusu": "tin tức", "keshimasu": "xóa", "tsukemasu": "bật", "un": "ừ", "uun": "hừm", "gomen": "xin lỗi",
        "sotsuka": "thế à", "mata": "lại"
    },
    "B8": {
        "udon": "mì udon", "soba": "mì soba", "kairo": "Cairo", "kotatsu": "bàn gắn lò sưởi", "zi": "chữ", "shotsuken": "phiếu ăn", "itadakimasu": "tôi xin phép ăn",
        "onakagaitsupaidesu": "tôi đói", "gochisousamadeshita": "cảm ơn vì bữa ăn", "ika": "dưới", "genkan": "cửa ra vào", "shitoberuto": "dây an toàn",
        "seifuku": "đồng phục", "baiku": "xe máy", "herumetsuto": "mũ bảo hiểm", "pasupoto": "hộ chiếu", "mihunshou": "giấy chứng minh nhân dân", "ryoukin": "tiền phí",
        "nyujouryou": "phí vào cửa", "narabimasu": "xếp hàng", "tomemasu": "dừng", "wakemasu": "chia", "kichinto": "đúng", "sounandesuka": "thế à", "hora": "này",
        "inaka": "nông thôn", "tokai": "thành phố", "kuuki": "không khí", "koutsuu": "giao thông", "zikyuu": "lương theo giờ", "ziyuu": "tự do", "dezein": "thiết kế",
        "bangumi": "chương trình", "fasutofudo": "đồ ăn nhanh", "fatsushon": "thời trang", "furipuran": "chương trình tự do", "omoimasu": "nghĩ", "supichikontesuto": "cuộc thi hùng biện",
        "i": "vị trí thứ", "saigo": "cuối cùng", "horu": "sảnh", "omoide": "kỷ niệm", "unazukimasu": "gật đầu", "kinchoushimasu": "hồi hộp", "waraimasu": "cười",
        "nanto": "dùng để nhấn mạnh", "garasu": "thủy tinh", "tomarimasu": "dừng", "hazimarimasu": "bắt đầu", "furimasu": "rơi", "kachimasu": "thắng", "makemasu": "thua",
        "taoremasu": "đổ", "dekimasu": "có thể", "otarashiimisegadekimasu": "cửa hàng mới được mở", "waremasu": "vỡ", "kowai": "sợ", "shinpai": "lo lắng", "kaze": "gió",
        "sutoratsupu": "dây đeo", "seki": "ghế", "isogimasu": "vội", "komimasu": "đông", "maniaimasu": "kịp", "yamimasu": "hết", "haremasu": "trời quang", "pasento": "phần trăm",
        "tsuyo": "mạnh", "kitsuto": "nhất định", "tabun": "có thể", "moshi": "nếu", "shimarimasu": "đóng", "sukimasu": "ít", "ochimasu": "rơi", "kiemasu": "biến mất",
        "kowaremasu": "hỏng", "yogoremasu": "bẩn", "kaijou": "hội trường", "kumori": "có mây", "taifuu": "bão", "zishin": "động đất", "ziko": "tai nạn", "taikai": "buổi họp",
        "chimu": "đội", "chuushi": "ngừng", "furimaketsuto": "chợ đồ cũ", "hantou": "thật", "mukashi": "ngày xưa", "urusai": "ồn ào", "oshiyare": "điệu", "fukuzatsu": "phức tạp",
        "benri": "tiện lợi", "itsudemo": "bất cứ lúc nào", "un": "vận may", "nitsuite": "về", "watashimosouomoimasu": "tôi cũng nghĩ thế", "chuurinjou": "giấy phép lái xe"
    },
    "B9": {
        "urusai": "ồn ào", "oshare": "điệu", "fukuzatsu": "phức tạp", "benri": "tiện lợi", "fuben": "bất tiện", "itsudemo": "lúc nào cũng", "un": "à", "nitsuite": "về",
        "tsuri": "tiền lẻ", "denki": "điện", "doa": "cửa", "tougarashi": "ớt", "fuuran": "chuông gió", "futon": "cái chăn", "poketsuto": "túi", "botan": "cái cúc",
        "yu": "nước nóng", "yutanpo": "bình sưởi ấm đựng nước sóng", "ruba": "cần gạt", "akimasu": "mở", "sawarimasu": "sờ", "tsukimasu": "bật", "mawashimasu": "xoay",
        "demasu": "ra", "otsurigademasu": "có tiền lẻ trả lại", "are": "ô", "otokonohito": "nam", "onnanohito": "nữ", "mise": "cửa hàng", "yuenchi": "công viên giải trí",
        "zietsutokosuta": "tàu lượn cao tốc", "denkiseihito": "đồ điện", "megane": "cái kính", "shatsu": "áo sơ mi", "sukato": "váy ngắn", "fukutai": "cà vạt", "boushi": "mũ",
        "ninki": "hâm mộ"
    }
}

class VocabularyQuiz:
    def __init__(self, root):
        self.root = root
        self.root.title("Trắc nghiệm Từ vựng Tiếng Nhật")
        self.score = 0
        self.current_question = 0
        self.words = []
        self.correct_meaning = ""
        self.options = []
        self.wrong_answers = []

        # Chạy bài kiểm tra đầu tiên
        self.start_quiz()
    
    def start_quiz(self):
        self.vocab_set = self.choose_vocab_set()
        if not self.vocab_set:
            self.root.quit()
            return
        
        self.words = list(self.vocab_set.keys())
        random.shuffle(self.words)
        
        self.total_questions = simpledialog.askinteger(
            "Số lượng câu hỏi",
            f"Nhập số lượng câu hỏi (tối đa {len(self.words)}):",
            parent=self.root,
            minvalue=1,
            maxvalue=len(self.words)
        )
        if not self.total_questions:
            self.total_questions = len(self.words)

        # Giao diện
        self.question_label = tk.Label(self.root, text="", font=("Arial", 16))
        self.question_label.pack(pady=20)

        self.option_buttons = []
        for i in range(4):
            button = tk.Button(self.root, text="", font=("Arial", 14), width=20, command=lambda i=i: self.check_answer(i))
            button.pack(pady=10)
            self.option_buttons.append(button)

        self.next_question()

    def choose_vocab_set(self):
        vocab_set_names = list(vocab_sets.keys())
        selected_set = simpledialog.askstring(
            "Chọn bộ từ vựng",
            f"Nhập tên bộ từ vựng ({', '.join(vocab_set_names)}):",
            parent=self.root
        )
        return vocab_sets.get(selected_set)

    def next_question(self):
        if self.current_question < self.total_questions:
            correct_word = self.words[self.current_question]
            self.correct_meaning = self.vocab_set[correct_word]
            self.options = random.sample(list(self.vocab_set.values()), 3)
            if self.correct_meaning not in self.options:
                self.options.append(self.correct_meaning)
            random.shuffle(self.options)

            self.question_label.config(text=f"Câu {self.current_question + 1}: Chọn nghĩa đúng của từ '{correct_word}':")
            for i in range(4):
                self.option_buttons[i].config(text=self.options[i])
        else:
            self.show_result()

    def check_answer(self, selected_index):
        if self.options[selected_index] == self.correct_meaning:
            self.score += 1
        else:
            self.wrong_answers.append((self.words[self.current_question], self.correct_meaning))
        self.current_question += 1
        self.next_question()

    def show_result(self):
        result_message = f"Bài thi kết thúc! Bạn đã trả lời đúng {self.score}/{self.total_questions} câu.\n\n"
        if self.wrong_answers:
            result_message += "Các từ bạn đã trả lời sai:\n"
            for word, meaning in self.wrong_answers:
                result_message += f"{word}: {meaning}\n"
        else:
            result_message += "Bạn đã trả lời đúng tất cả các câu hỏi!"

        messagebox.showinfo("Kết thúc", result_message)
        self.ask_next_quiz()
    
    def ask_next_quiz(self):
        next_set = simpledialog.askstring(
            "Chọn bộ từ vựng tiếp theo",
            f"Bạn có muốn làm tiếp bộ khác không? ({', '.join(vocab_sets.keys())}) Nếu không, nhập 'Không'.",
            parent=self.root
        )
        
        if next_set and next_set in vocab_sets:
            self.score = 0
            self.current_question = 0
            self.words = []
            self.correct_meaning = ""
            self.options = []
            self.wrong_answers = []
            self.vocab_set = vocab_sets[next_set]
            self.words = list(self.vocab_set.keys())
            random.shuffle(self.words)
            self.total_questions = min(len(self.words), self.total_questions)
            self.next_question()
        else:
            self.root.quit()

if __name__ == "__main__":
    root = tk.Tk()
    root.geometry("500x400")
    app = VocabularyQuiz(root)
    root.mainloop()
