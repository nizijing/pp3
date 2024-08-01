# 首先，定义原始接口（老式音频播放器接口）
class OldMediaPlayer:
    def play_vinyl(self):
        print("Playing vinyl...")

# 然后，定义新的音频服务接口和其实现
class NewAudioService:
    def play_song(self, song_name):
        print(f"Playing {song_name} from new audio service...")

# 创建适配器，使其符合老式音频播放器的接口，但实际使用新的音频服务
class NewAudioServiceAdapter:
    def __init__(self, new_audio_service):
        self.new_audio_service = new_audio_service

    def play_vinyl(self):
        # 将播放黑胶唱片的方法适配为播放新音频服务的歌曲
        self.new_audio_service.play_song("Vinyl Song")

# 使用适配器
new_audio_service = NewAudioService()
adapter = NewAudioServiceAdapter(new_audio_service)

old_player = OldMediaPlayer()
# 直接使用老式播放器无法播放新音频服务的内容
# old_player.play_vinyl()  # 播放黑胶唱片

# 通过适配器，老式播放器现在可以播放新音频服务的内容
adapter.play_vinyl()  # 输出：Playing Vinyl Song from new audio service...