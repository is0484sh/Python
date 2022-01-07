//Update for Unity2019 on 5.21.2020

using UnityEngine;
using System.Collections;

public class First_Velocity : MonoBehaviour {

	// Use this for initialization
	void Start () {
//		rigidbody.velocity = new Vector3 (0.0f,2.0f,0.0f);
		GetComponent<Rigidbody>().velocity = new Vector3 (0.0f,2.0f,0.0f);
	
	}
	
	// Update is called once per frame
	void Update () {
	
	}
}
