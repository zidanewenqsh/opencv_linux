#include "main.h"
#include "test.h"
#include "demo.h"
#include "utils.h"

int main(int argc, char *argv[])
{
	cout << "hello world" << endl;
	string imgpath = "cat01.jpg";
	cv::Mat img = cv::imread(imgpath, 1);
	cv::imshow("img", img);
	cv::waitKey(0);

	return 0;
}
