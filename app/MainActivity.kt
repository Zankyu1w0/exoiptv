package com.example.exoiptv

import android.os.Bundle
import androidx.appcompat.app.AppCompatActivity
import com.google.android.exoplayer2.ExoPlayer
import com.google.android.exoplayer2.MediaItem
import com.google.android.exoplayer2.ui.StyledPlayerView

class MainActivity : AppCompatActivity() {
    private var player: ExoPlayer? = null

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        
        // Ekrana sadece video oynatıcıyı koyuyoruz
        val playerView = StyledPlayerView(this)
        setContentView(playerView)

        // ExoPlayer'ı (Oynatıcıyı) oluşturuyoruz
        player = ExoPlayer.Builder(this).build()
        playerView.player = player

        // Senin verdiğin TRT 1 bağlantısı
        val trtHatti = "https://tv-trt1.medya.trt.com.tr/master.m3u8"
        val mediaItem = MediaItem.fromUri(trtHatti)
        
        player?.setMediaItem(mediaItem)
        player?.prepare()
        player?.play()
    }

    override fun onDestroy() {
        super.onDestroy()
        player?.release()
    }
}
