![](https://i.imgur.com/Y80SpfK.jpg)

twitch-scheduler는 github action을 기반으로 실행되는 트위치 vod 다운로더 스케줄러입니다.  
Read this in other languages: [한국어](README.ko.md) [english](README.md)

---

## 주요 기능

+ 원하는 화질로 언제 어디서나 vpn 없이 트위치 vod 다운로드 요청 가능
+ gtihub action을 활용하여 정해진 스케줄에 다운로드 요청 가능
+ 특정한 채널의 vod를 중복없이 다운로드 가능
+ 동영상 병합 시 채팅창 병합 가능(선택적)
+ ffmpeg를 이용하여 원하는 옵션으로(동영상 압축, 배너 달기 등) 동영상 편집 가능

---

## 사용 방법

You can get this application from the Official SongTube Channel on **Telegram:** https://t.me/songtubechannel **You can also join SongTube Official Group from the Channel, any kind of issue report or recommendation is welcomed!**

Other SongTube download sites:

+ Drive: https://tinyurl.com/SongTubeDrive
+ GitHub: https://tinyurl.com/STGithub
+ AppGallery: https://tinyurl.com/STAppGallery

---

## How to Update NewPipeExtractor_Dart(Library for Youtube)

**1st Step:** Select NewPipeExtractor(including forks) you want to use

- NewPipe [NewPipeExtractor](https://github.com/TeamNewPipe/NewPipeExtractor)
- AnimePipe [NewPipeExtractor](https://github.com/InfinityLoop1309/NewPipeExtractor)
- SkyTube [NewPipeExtractor](https://github.com/SkyTubeTeam/NewPipeExtractor)
- And Other Forks [Click this link to see Active Forks](https://techgaun.github.io/active-forks/index.html#TeamNewPipe/NewPipeExtractor)

**2nd Step:** Update NewPipeExtractor to NewPipeExtractor_Dart

Find build.gradle under **NewPipeExtractor_Dart\android** folder.  
Than Find line ``implementation 'com.github.SkyTubeTeam.NewPipeExtractor:NewPipeExtractor:LOCAL_SNAPSHOT'``  
Change the dependency version you want to use
```gradle
// NewPipe
implementation 'com.github.TeamNewPipe:NewPipeExtractor:v0.20.10'

// Skytube
implementation 'com.github.SkyTubeTeam.NewPipeExtractor:NewPipeExtractor:skytube-2022-11-04'
```