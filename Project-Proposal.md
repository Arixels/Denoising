# Project Proposal

The project proposal is a critical document laying out the specification for a research project. It is the first deliverable in any research program, and will often be dynamically updated over the course of the project. It is likely to become a part of a future writeup / academic paper.

## Big picture
- What is the overall problem that this and related research is trying to solve?
- Why should people care about the problem?
- What has been done so far to solve this problem?

## Specific project scope
- What subset of the overall problem are you addressing in particular?
- How does solving this subproblem lead towards solving the big picture problem?
- What is your specific approach to solving this subproblem?
- How will this approach result in a solution?
- How will we know that this subproblem has been satisfactorily solved, using quantitative metrics?
- Create and include one or two graphics that capture and communicate the problem and proposed solution to technical but non-expert audiences.

*Can you create a one or two sentence summary of the problem and the proposed solution approach?*

## Broader impact
- What is the value of your approach beyond this specific solution?
- What is the value of this solution beyond solely solving this subproblem and getting us closer to solving the big picture problem?
- In other words, even if someone doesn't care about the big picture problem that you started with, why should they still care about the specific work that you've produced? Who else can use your processes and results, and how?

## Background / related work / references
- Find external sources that support your framing of the research problem. In particular, you should establish your answers to all of the above questions using only material from other researchers.
- You should also find additional sources that address:
  - What foundation and fundamentals need to be known in order to understand your problem, approach, and solution?
  - What work has been done before on this specific problem?
  - What are related problems that have been addressed, and what work has been done on those?
  - What are unrelated problems that have employed specific aspects of your proposed approach or solution?
  - How does this collection of past work contribute to your planned work?
  - How do we know that your subproblem hasn't yet been solved?
- Be sure to cite all potential sources, and summarize each one in terms of its content and relation to your project.

## Capabilities, deliverables, tasks
- Recursively break down the proposed project starting from the highest level specifications spanning the complete research period down to individual atomic steps spanning days to at most a week. At each level of hierarchy, specify:
  - What capabilities does your system need to achieve?
  - What is an (engineering) outcome that is currently not achievable that this capability will make possible?
  - What are the specific academic questions that this will answer?
  - What deliverables will you produce to indicate that the above capabilities have been achieved? *(These must be specific, concrete nouns.)*
  - How do these deliverables prove that the capabilities have been met?
  - How do these deliverables prove that there is no way the capabilities cannot have been met?
  - What tasks are necessary to generate those deliverables? *(These must include specific, concrete verbs that you as an engineer must do.)*
  - Include as much detail as you can, so you can properly predict the time to allocate for each task, and prepare for anticipated contingencies.
  - Be sure to include dependencies --- which (earlier) capabilities must your system be capable of in order for you to start each task?
- Distill the entire hierarchy into a list of weekly or shorter milestones. What will you need to achieve by when in order to attain your objectives for the end of the project on time?

*Keep in mind that these capabilities, deliverables, and tasks are all distinct characterizations of required research. Tasks are verbs that you as the engineer must fulfill. They are done in order to enable your engineered system to accomplish its desired capabilities. In order for your system to achieve a single capability, you may need to execute several subtasks; each of your subtasks may have required your system to have accomplished a sub-capability enabling an incremental update in its abilities. The collection of deliverables should be sufficient for someone who hasn't seen you working to certify that your capabilities have been met, and your system can in fact achieve the prescribed abilities. When generating deliverables, keep in mind that one data point does not indicate a trend, and appropriate statistical rigor should be applied to the presented results. Try to address counterfactuals, edge cases, and competing explanations in your deliverables.*

*As an example:*

*Capability: The robot can computationally estimate its [x, y, θ] state in real time; or our system can compute an error metric on the robot's real-time state estimate.*
*Deliverables:*
- *Video showing robot being controlled randomly by human driver, with a view of an overhead camera image being used for ground truth measurements; a real-time display of the estimated position will be overlaid onto that view*
- *Several trajectory plots of ground truth position along with estimated position from varying initial conditions under varying control input sequences*
- *Shaded statistical plot of Euclidean error and angular heading error over time for those trajectories*
*Tasks:*
- *Learn Kalman filtering*
- *Program KF in Python*
- *Connect inputs and outputs of robot car into KF code*
- *Compute ground truth from overhead camera using OpenCV*
- *Draw output of KF as overlay on overhead camera view*
- *Generate relevant plots of results*

*A bad example:*

*(not a) capability: Program a Kalman filter (this is not a question that you are looking to answer, nor an ability of the system that you are engineering)*
*(not a) deliverable: KF code listing (this does not certify that the code enables the ability it is meant to do, nor even that it compiles or is complete)*
*(not a) task: Run KF code (I guess this could sort of be a task, but if all this means is pushing "go", you're not really detailing what it is you need to spend time on)*
