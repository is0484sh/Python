// Unity DataOutput 関数　（2016/03/29）
// UpdatePoint
// ・ファイルオープンを最初に実施
// ・データ出力を物理エンジンの更新タイミングで実施
//    メニューバー の Edit -> Project Settings −＞ Time −＞ Fixed Timestep
//　　で、設定値を0.01秒に設定して、Linux環境と一致させる
//

using UnityEngine;
using System.Collections;
using System.IO;
using System.Text;

public class Output : MonoBehaviour {
	public string filename;
	private FileStream f; 
	private Encoding utf8Enc; 
	private StreamWriter writer;
	private float time;

	// Start() is called at the first CG frame.
	void Start () {
	}

	// Use this for initialization
	// Awake() is called when the instance is initiated.
	void Awake(){
		f = new FileStream(filename+".csv", FileMode.Create, FileAccess.Write);
		utf8Enc = Encoding.GetEncoding ("UTF-8");
	    writer = new StreamWriter (f, utf8Enc);
		time = 0.0f;
	}

	// Update is called once on fixed timing. Timing is defined on project setting
	void FixedUpdate () {
		writer.WriteLine (time * 1000 + "," + transform.position.y);
		time += Time.deltaTime;
	}

	// OnApplicatinoQuit() is called when this application is quited.
	void OnApplicationQuit(){
		writer.Close ();
	}
}
