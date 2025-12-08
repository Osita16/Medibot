# Contributing to Medibot

Thank you for your interest in contributing to Medibot! This document provides guidelines and instructions for contributing.

## Ways to Contribute

- **Bug Reports**: Report bugs by opening an issue
- **Feature Requests**: Suggest new features or improvements
- **Code Contributions**: Submit pull requests with bug fixes or new features
- **Documentation**: Improve documentation, tutorials, or examples
- **Testing**: Test the system and provide feedback

## Getting Started

1. Fork the repository
2. Clone your fork:
   ```bash
   git clone https://github.com/YOUR_USERNAME/Medibot.git
   cd Medibot
   ```

3. Set up the development environment:
   ```bash
   source /opt/ros/humble/setup.bash
   ./setup.sh
   ```

4. Create a new branch for your feature:
   ```bash
   git checkout -b feature/your-feature-name
   ```

## Development Guidelines

### Code Style

- Follow [ROS2 Python Style Guide](https://docs.ros.org/en/humble/The-ROS2-Project/Contributing/Code-Style-Language-Versions.html)
- Use meaningful variable and function names
- Add docstrings to functions and classes
- Keep functions small and focused

### Package Organization

The project is organized into three main packages:

1. **medibot_description**: Robot URDF models and description files
2. **medibot_gazebo**: Simulation world and launch files
3. **medibot_navigation**: Navigation configuration and scripts

### Testing

Before submitting a pull request:

1. Build the workspace:
   ```bash
   colcon build
   source install/setup.bash
   ```

2. Test the simulation:
   ```bash
   ros2 launch medibot_gazebo hospital_simulation.launch.py
   ```

3. Test navigation (if applicable):
   ```bash
   ros2 launch medibot_navigation full_navigation.launch.py
   ```

## Submitting Changes

1. Commit your changes with clear, descriptive messages:
   ```bash
   git commit -m "Add: Brief description of what you added"
   ```

2. Push to your fork:
   ```bash
   git push origin feature/your-feature-name
   ```

3. Create a Pull Request:
   - Go to the original repository
   - Click "New Pull Request"
   - Select your branch
   - Provide a clear description of your changes

### Pull Request Guidelines

- **Title**: Clear and descriptive
- **Description**: Explain what changes you made and why
- **Testing**: Describe how you tested your changes
- **Screenshots**: Include screenshots for UI/visual changes

## Reporting Bugs

When reporting bugs, please include:

- **System Information**:
  - ROS2 version
  - Ubuntu version
  - Gazebo version

- **Steps to Reproduce**:
  1. What commands did you run?
  2. What did you expect to happen?
  3. What actually happened?

- **Error Messages**: Include full error messages and logs

- **Additional Context**: Screenshots, videos, or other relevant information

## Feature Requests

When requesting features, please:

- Check if the feature already exists
- Explain the use case and why it would be valuable
- Provide examples or mockups if applicable

## Areas for Contribution

Here are some areas where contributions are especially welcome:

### High Priority
- [ ] Multi-floor navigation support
- [ ] Dynamic obstacle avoidance improvements
- [ ] Better path planning algorithms
- [ ] Performance optimization

### Medium Priority
- [ ] Additional hospital rooms and areas
- [ ] More robot models
- [ ] Advanced sensor integration
- [ ] Improved visualization in RViz

### Low Priority (Nice to Have)
- [ ] Multi-robot coordination
- [ ] Patient tracking system
- [ ] Integration with hospital databases
- [ ] Mobile app control interface

## Code Review Process

1. A maintainer will review your pull request
2. They may request changes or ask questions
3. Once approved, your PR will be merged
4. Your contribution will be credited

## Community Guidelines

- Be respectful and constructive
- Help others learn and grow
- Focus on the code, not the person
- Ask questions when unclear

## License

By contributing to Medibot, you agree that your contributions will be licensed under the Apache License 2.0.

## Questions?

If you have questions:
- Open an issue for discussion
- Check existing issues and documentation
- Reach out to maintainers

## Acknowledgments

Thank you for contributing to making hospital automation better!
