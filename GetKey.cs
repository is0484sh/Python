using UnityEngine;
using System.Collections;

public class GetKey: MonoBehaviour {

	// Use this for initialization
	void Start () {
	
	}
	
	// Update is called once per frame
	void Update () {
		if (Input.GetKey("up")) {
			transform.Rotate (1f,0f,0f);
		}
		if (Input.GetKey("down")) {
			transform.Rotate (-1f,0f,0f);
		}
		if (Input.GetKey("right")) {
			transform.Rotate (0f,0f,-1f);
		}
		if (Input.GetKey("left")) {
			transform.Rotate (0f,0f,1f);
		}
	}
}
