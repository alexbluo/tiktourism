import "package:flutter/material.dart";
import "package:font_awesome_flutter/font_awesome_flutter.dart";

class ScrollItem extends StatelessWidget {
  const ScrollItem({Key? key}) : super(key: key);

  @override
  Widget build(BuildContext context) {
    final size = MediaQuery.of(context).size;

    void _like() {
      print("hi");
    }

    return GestureDetector(
      onDoubleTap: _like,
      child: Stack(
        clipBehavior: Clip.none,
        children: <Widget>[
          const Center(
            child: FaIcon(
              FontAwesomeIcons.solidHeart,
              color: Colors.red,
            ),
          ),
          Container(
            padding: const EdgeInsets.all(12),
            child: Align(
              alignment: Alignment.centerRight,
              child: Column(
                mainAxisAlignment: MainAxisAlignment.center,
                children: const [
                  FaIcon(FontAwesomeIcons.heart, color: Colors.red),
                ],
              ),
            ),
          ),

          // Container(
          //   width: size.width,
          //   height: size.height,
          //   decoration: const BoxDecoration(
          //     color: Colors.black,
          //   ),
          //   child: const Image(
          //     image: NetworkImage(
          //         "https://flutter.github.io/assets-for-api-docs/assets/widgets/owl.jpg"),
          //   ),
          // ),
        ],
      ),
    );
  }
}
